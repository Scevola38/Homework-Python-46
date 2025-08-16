from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Открыть браузер Google Chrome
driver = webdriver.Chrome()

# Перейти на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Кликнуть на синюю кнопку
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()