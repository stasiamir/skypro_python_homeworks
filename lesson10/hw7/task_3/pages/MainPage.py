import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует главную страницу.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Добавление товаров в корзину")
    def add_to_cart(self) -> None:
        """
        Добавляет товары в корзину.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()