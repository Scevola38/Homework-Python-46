from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открываем браузер FireFox
browser = webdriver.Firefox()

# Переходим на страницу
browser.get('http://the-internet.herokuapp.com/login')

# Находим поля для ввода логина и пароля, вводим значения
username_field = browser.find_element(By.ID, "username")
username_field.send_keys('tomsmith')

password_field = browser.find_element(By.ID, 'password')
password_field.send_keys('SuperSecretPassword!')

# Нажимаем кнопку Login
login_button = browser.find_element(By.CSS_SELECTOR, '.fa-sign-in')
login_button.click()

# Находим зеленую плашку и выводим текст
success_message = browser.find_element(By.CSS_SELECTOR, '.flash.success')
print(success_message.text)

# Закрываем браузер
browser.quit()
