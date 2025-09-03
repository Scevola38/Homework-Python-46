import requests

base_url = "https://yougile.com/api-v2"
# Укажите свой известный токен (получаем его, запуская key_get.py)
token = 't2QyAjAQw-3mmzUxwKGtu9u-eKpq3XrKj23e0GtJU0AdonxCTlLk7tl-Ct0X7Mw7'


# Позитивные тесты
def test_get_projects():
    headers = {
        'Authorization': f'Bearer {token}'
    }

    resp = requests.get(base_url + '/projects', headers=headers)
    body = resp.json()
    assert resp.status_code == 200
    assert len(body) > 0

    project = body["content"][0]
    users = project["users"]
    return users


def test_create_project():
    users = test_get_projects()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "title": "TestCreate",
        "users": users
    }

    resp = requests.post(base_url + '/projects',
                         headers=headers, json=project_data)

    assert resp.status_code == 201
    project_id = resp.json()["id"]
    return project_id


def test_get_project_by_id():
    project_id = test_create_project()

    headers = {
        'Authorization': f'Bearer {token}'
    }

    resp = requests.get(f"{base_url}/projects/{project_id}", headers=headers)

    assert resp.status_code == 200


def test_update_project():
    project_id = test_create_project()

    users = test_get_projects()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "deleted": True,
        "title": "TestUpdate",
        "users": users
    }

    resp = requests.put(f"{base_url}/projects/{project_id}",
                        headers=headers, json=project_data)

    assert resp.status_code == 200


# Негативные тесты
def test_create_project_without_title():
    users = test_get_projects()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "users": users
    }

    resp = requests.post(base_url + '/projects',
                         headers=headers, json=project_data)

    assert resp.status_code == 400


def test_create_project_without_info():
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
    }

    resp = requests.post(base_url + '/projects',
                         headers=headers, json=project_data)

    assert resp.status_code == 400


def test_update_project_without_title():
    users = test_get_projects()

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "deleted": True,
        "users": users
    }

    resp = requests.put(f"{base_url}/projects/",
                        headers=headers, json=project_data)

    assert resp.status_code == 404


def test_update_project_without_users():
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    project_data = {
        "deleted": True,
        "title": "TestUpdate"
    }

    resp = requests.put(f"{base_url}/projects/",
                        headers=headers, json=project_data)

    assert resp.status_code == 404
