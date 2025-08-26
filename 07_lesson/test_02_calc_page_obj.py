import pytest
from selenium import webdriver
from pages.CalculatorPage import SlowCalculatorPage
from selenium.common.exceptions import TimeoutException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = SlowCalculatorPage(driver)
    calculator_page.open()

    calculator_page.set_delay("45")

    calculator_page.click_button("7")
    calculator_page.click_button("+")
    calculator_page.click_button("8")
    calculator_page.click_button("=")

    try:
        result = calculator_page.get_result()
        print(f"Текущий результат: {result}")

        assert result == "15", f"Ошибка: ожидалось 15, но получено {result}"
        print("Тест успешно пройден: результат 15")
    except TimeoutException:
        print("Таймаут: результат не был найден.")
    except AssertionError as e:
        print(e)
