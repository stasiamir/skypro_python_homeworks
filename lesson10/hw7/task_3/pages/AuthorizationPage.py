import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AuthorizationPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу авторизации.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    @allure.step("Ввод имени пользователя: {value}")
    def username(self, value: str) -> None:
        """
        Вводит имя пользователя на странице авторизации.

        :param value: Имя пользователя для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(value)

    @allure.step("Ввод пароля: {value}")
    def password(self, value: str) -> None:
        """
        Вводит пароль на странице авторизации.

        :param value: Пароль для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(value)

    @allure.step("Нажатие кнопки входа")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа на странице авторизации.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()