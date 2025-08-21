import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и закрытия драйвера Chrome.
    """
    driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver находится в PATH
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    """
    Тест для проверки медленного калькулятора на странице.
    """
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения задержки
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.send_keys("45")

    # Нажатие на кнопки
    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()
    plus_button = driver.find_element(By.XPATH, "//span[text()='+']")
    plus_button.click()
    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    equal_button = driver.find_element(By.XPATH, "//span[text()='=']")
    equal_button.click()

    # Ожидание появления результата
    result_locator = (By.ID, "result")
    WebDriverWait(driver, 50).until(EC.text_to_be_present_in_element(result_locator, "15"))

    # Проверка результата
    result_element = driver.find_element(*result_locator)
    assert result_element.text == "15", f"Ожидался результат '15', но получен '{result_element.text}'"


if __name__ == "__main__":
    pytest.main([__file__])
