import pytest
from selenium import webdriver
from pages.shopPage import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_shop_demo(driver):
    page = ShopPage(driver)
    page.login("standard_user", "secret_sauce")
    page.add_items_to_cart()
    page.go_to_cart()
    page.checkout("Имя", "Фамилия", "12345")

    total_price = page.get_total_price()
    assert total_price == "Total: $58.29", (f"Итоговая сумма отличается:"
                                            f" {total_price}")
    print("Итоговая сумма верна!")
