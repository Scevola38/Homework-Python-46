from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.edge.service import Service as EdgeService
import pytest


@pytest.fixture(scope="module")
def driver():
    service = EdgeService(
        executable_path="C:\\Users\\Юзер\\Downloads\\edgedriver_win64\\"
                        "msedgedriver.exe")
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def test_data_types_form(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")  # Оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Отправляем форму
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Проверяем появление элемента с ошибкой для zip-code
    try:
        # Явное ожидание: ждем, пока появится элемент div с id="zip-code"
        zip_code_error_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        # Проверяем, что текст элемента равен "N/A"
        assert (zip_code_error_element.text ==
                "N/A"), "Текст элемента zip-code не соответствует ожидаемому"

    except TimeoutException:
        pytest.fail("Не дождались появления элемента div с id='zip-code'")
