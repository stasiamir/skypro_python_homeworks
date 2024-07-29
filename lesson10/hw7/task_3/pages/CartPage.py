import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу корзины.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Переход в корзину")
    def get_to_cart(self) -> None:
        """
        Переходит на страницу корзины.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container>a').click()

    @allure.step("Переход к оформлению заказа")
    def get_to_checkout(self) -> None:
        """
        Переходит на страницу оформления заказа.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()