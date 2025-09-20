import pytest
from selenium import webdriver
from pages.shopPage import ShopPage
import allure
from allure_commons.types import Severity


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Тест покупки товаров в магазине")
@allure.description(
    "Проверка успешного оформления заказа в магазине с добавлением товаров в корзину и проверкой итоговой суммы.")
@allure.feature("Оформление заказа")
@allure.severity(Severity.CRITICAL)
def test_shop_demo(driver):
    with allure.step("Инициализация страницы магазина"):
        page = ShopPage(driver)

    with allure.step("Выполнение логина пользователя"):
        page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        page.add_items_to_cart()

    with allure.step("Переход в корзину"):
        page.go_to_cart()

    with allure.step("Заполнение данных для оформления заказа"):
        page.checkout("Имя", "Фамилия", "12345")

    with allure.step("Получение итоговой суммы"):
        total_price = page.get_total_price()

    with allure.step("Проверка итоговой суммы"):
        assert total_price == "Total: $58.29", (f"Итоговая сумма отличается:"
                                                f" {total_price}")
        print("Итоговая сумма верна!")
