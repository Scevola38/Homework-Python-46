from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Google Chrome
driver = webdriver.Chrome()

# Переходим на страницу
driver.get("http://uitestingplayground.com/classattr")

# Находим и кликаем на синюю кнопку
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

# Закрываем браузер
driver.quit()