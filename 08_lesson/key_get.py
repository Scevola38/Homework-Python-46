import requests

base_url = "https://yougile.com/api-v2"


def get_company_id():
    creds = {
        'login': 'stivenfrai38@mail.ru',  # Укажите свой email
        'password': 'Margerit39!',  # Укажите свой пароль
        'name': "СкайПро"  # Укажите название своей компании
    }
    resp = requests.post(base_url + '/auth/companies', json=creds)
    if resp.status_code == 200:
        companyID = resp.json()["content"][0]["id"]
        return companyID
    else:
        print(f"Ошибка при получении companyID: {resp.status_code}")
        return None


def get_key():
    companyID = get_company_id()

    if companyID is None:
        return None

    key_data = {
        'login': 'stivenfrai38@mail.ru',  # Укажите свой email
        'password': 'Margerit39!',  # Укажите свой пароль
        'companyId': companyID
    }

    resp = requests.post(base_url + '/auth/keys', json=key_data)

    if resp.status_code == 201:
        key = resp.json()['key']
        return key
    else:
        print(f"Ошибка при получении ключа: {resp.status_code}")
        return None


if __name__ == "__main__":
    key = get_key()

    if key:
        print(f"Ваш ключ: {key}")
    else:
        print("Не удалось получить ключ.")
