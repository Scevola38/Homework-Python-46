import pytest
from selenium import webdriver
from pages.CalculatorPage import SlowCalculatorPage
from selenium.common.exceptions import TimeoutException
import allure
from allure_commons.types import Severity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверяет корректность сложения чисел в калькуляторе с установленной задержкой.")
@allure.feature("Калькулятор")
@allure.severity(Severity.NORMAL)
def test_calculator(driver):
    with allure.step("Инициализация страницы калькулятора"):
        calculator_page = SlowCalculatorPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        calculator_page.open()

    with allure.step("Установка задержки"):
        delay = "25"
        calculator_page.set_delay(delay)
        allure.attach(delay.encode('utf-8'), name="Установленная задержка (сек)",
                      attachment_type=allure.attachment_type.TEXT)

    with allure.step("Ввод первого числа"):
        calculator_page.click_button("7")

    with allure.step("Нажатие кнопки сложения"):
        calculator_page.click_button("+")

    with allure.step("Ввод второго числа"):
        calculator_page.click_button("8")

    with allure.step("Нажатие кнопки равно"):
        calculator_page.click_button("=")

    with allure.step("Ожидание и получение результата"):
        expected_result = "15"
        try:
            WebDriverWait(driver, 40).until(
                EC.text_to_be_present_in_element((By.ID, "result"), expected_result)
            )

            with allure.step("Получение фактического результата"):
                actual_result = calculator_page.get_result()

            with allure.step("Проверка результата"):
                assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"
                print("Тест успешно пройден: результат 15")

        except TimeoutException:
            allure.attach(driver.get_screenshot_as_png(), name="timeout_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            print("Таймаут: результат не появился вовремя.")
            pytest.fail("Таймаут: результат не появился вовремя.")  # Используем pytest.fail
        except AssertionError as e:
            allure.attach(driver.get_screenshot_as_png(), name="assertion_error_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            print(e)
            pytest.fail(str(e))  # Используем pytest.fail и передаем сообщение об ошибке
