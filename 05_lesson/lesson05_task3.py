from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Открываем браузер FireFox
driver = webdriver.Firefox()

# Переходим на страницу http://the-internet.herokuapp.com/inputs
driver.get("http://the-internet.herokuapp.com/inputs")

# Находим поле ввода и вводим текст "Sky"
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("Sky")

# Ждем 2 секунды
time.sleep(2)

# Очищаем поле ввода
input_field.clear()

# Ждем 2 секунды
time.sleep(2)

# Вводим текст "Pro"
input_field.send_keys("Pro")

# Ждем 2 секунды
time.sleep(2)

# Закрываем браузер
driver.quit()