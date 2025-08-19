from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера Chrome
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открываем веб-страницу
driver.get("http://uitestingplayground.com/textinput")

# Находим поле ввода по тегу input
input_field = driver.find_element(By.TAG_NAME, "input")

# Вводим текст "SkyPro" в поле ввода
input_field.send_keys("SkyPro")

# Находим кнопку по id и получаем текст после нажатия
button = driver.find_element(By.ID, "updatingButton")
button_text_before = button.text
button.click()
button_text_after = button.text

# Проверяем, изменился ли текст кнопки
if button_text_before != button_text_after:
    print('("SkyPro")')
else:
    print('("SkyPro")')

# Закрываем браузер после завершения
driver.quit()
