from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculatorPage:
    """
    Класс, представляющий страницу медленного калькулятора.
    """

    def __init__(self, driver):
        """
        Конструктор класса.

        Args:
            driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver

    def open(self):
        """
        Открывает страницу медленного калькулятора в веб-браузере.

        Returns:
            None
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, delay: str):
        """
        Устанавливает задержку для калькулятора.

        Args:
            delay (str): Значение задержки в виде строки (например, "5").

        Returns:
            None
        """
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text: str):
        """
        Кликает на кнопку на странице калькулятора.

        Args:
            button_text (str): Текст на кнопке, которую нужно нажать (например, "1", "+", "=").

        Returns:
            None
        """
        buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                            "span.btn.btn-outline-primary,"
                                            " span.operator.btn."
                                            "btn-outline-success,"
                                            " span.btn.btn-outline-warning")
        for button in buttons:
            if button.text == button_text:
                button.click()
                break

    def get_result(self) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        Returns:
            str: Результат вычисления в виде строки.
        """
        WebDriverWait(self.driver, 90).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen")))
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text
