from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ShopPage:
    """
    Класс, представляющий страницу магазина saucedemo.com.
    Содержит методы для авторизации, добавления товаров в корзину,
    перехода в корзину, оформления заказа и получения общей стоимости.
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализирует объект ShopPage.

        Args:
            driver (WebDriver): Объект WebDriver для управления браузером.
        """
        self.driver = driver

    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход пользователя на сайт saucedemo.com.

        Args:
            username (str): Имя пользователя.
            password (str): Пароль пользователя.

        Returns:
            None
        """
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        ).send_keys(password)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        ).click()

    def add_items_to_cart(self) -> None:
        """
        Добавляет предопределенный набор товаров в корзину.

        Returns:
            None
        """
        items_to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for item in items_to_add:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, item))
            ).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        Returns:
            None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        ).click()

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        """
        Выполняет оформление заказа, заполняя данные пользователя.

        Args:
            first_name (str): Имя пользователя.
            last_name (str): Фамилия пользователя.
            postal_code (str): Почтовый индекс.

        Returns:
            None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        ).send_keys(last_name)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        ).send_keys(postal_code)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        ).click()

    def get_total_price(self) -> str:
        """
        Получает строку с итоговой стоимостью заказа.

        Returns:
            str: Текст, содержащий итоговую стоимость заказа.
        """
        total_price_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "summary_total_label"))
        )
        return total_price_element.text
