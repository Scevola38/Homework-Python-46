import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():

    service = FirefoxService(executable_path="C:/Users/Юзер/Downloads/"
                                             "geckodriver-v0.36.0-win64/"
                                             "geckodriver.exe")
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_purchase_flow(driver):
    """
    Тест, автоматизирующий процесс покупки на saucedemo.com
    и проверяющий итоговую сумму.
    """

    # 1. Открытие сайта магазина
    driver.get("https://www.saucedemo.com/")

    # 2. Авторизация
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # 3. Добавление товаров в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        add_to_cart_button = driver.find_element(
            By.XPATH,
            f"//div[text()='{item_name}']/"
            f"ancestor::div[@class='inventory_item']//"
            f"button[text()='Add to cart']"
        )
        add_to_cart_button.click()

    # 4. Переход в корзину
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()

    # 5. Нажатие Checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # 6. Заполнение формы
    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    postal_code_field = driver.find_element(By.ID, "postal-code")
    continue_button = driver.find_element(By.ID, "continue")

    first_name_field.send_keys("Dmitriy")
    last_name_field.send_keys("Sokolov")
    postal_code_field.send_keys("307170")
    continue_button.click()

    # 7. Получение итоговой стоимости
    try:
        total_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".summary_total_label"))
        )
    except Exception as e:
        driver.save_screenshot("error.png")
        print(f"Ошибка при поиске элемента: {e}")
        raise

    total_text = total_element.text
    total_value = float(total_text.split("$")[1])

    # 8. Проверка итоговой суммы
    expected_total = 58.29
    assert abs(total_value - expected_total) < 0.01, (
        f"Итоговая сумма не совпадает. "
        f"Ожидалось:{expected_total}, "
        f"Получено: {total_value}"
    )
