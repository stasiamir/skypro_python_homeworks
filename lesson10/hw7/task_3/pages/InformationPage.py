import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InformationPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу информации.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Добавление имени: {value}")
    def add_first_name(self, value: str) -> None:
        """
        Вводит имя на странице информации.

        :param value: Имя для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(value)

    @allure.step("Добавление фамилии: {value}")
    def add_last_name(self, value: str) -> None:
        """
        Вводит фамилию на странице информации.

        :param value: Фамилия для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(value)

    @allure.step("Добавление почтового индекса: {value}")
    def add_zip_code(self, value: str) -> None:
        """
        Вводит почтовый индекс на странице информации.

        :param value: Почтовый индекс для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(value)

    @allure.step("Нажатие кнопки продолжить")
    def click_button(self) -> None:
        """
        Нажимает кнопку "Продолжить" на странице информации.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()