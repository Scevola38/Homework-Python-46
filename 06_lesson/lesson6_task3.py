import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

waiter = WebDriverWait(driver, 30)

waiter.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                  "#landscape")))

src_url = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

file_name = os.path.basename(src_url)
desired_format = "img/" + file_name
print(desired_format)

driver.quit()
