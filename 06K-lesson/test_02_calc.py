from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    # Указываем путь к нашему ChromeDriver
    chrome_driver_path = ("C:\\Users\\Юзер\\Downloads\\chromedriver-win64\\"
                          "chromedriver-win64\\chromedriver.exe")

    # Создаем экземпляр Service с указанием пути к драйверу
    service = Service(executable_path=chrome_driver_path)

    # Инициализируем драйвер Chrome с использованием Service
    driver = webdriver.Chrome(service=service)

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/"
               "slow-calculator.html")

    # Вводим значение задержки
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очищаем поле, если там что-то есть
    delay_input.send_keys("45")

    # Нажимаем кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидаем, пока результат не отобразится
    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверяем, что результат равен 15
    assert driver.find_element(By.CSS_SELECTOR, ".screen").text == "15"
    driver.quit()
