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
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    @allure.step("Ввод имени: {value}")
    def first_name(self, value: str) -> None:
        """
        Вводит имя в форму.

        :param value: Имя для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='first-name']").send_keys(value)

    @allure.step("Ввод фамилии: {value}")
    def last_name(self, value: str) -> None:
        """
        Вводит фамилию в форму.

        :param value: Фамилия для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='last-name']").send_keys(value)

    @allure.step("Ввод адреса: {value}")
    def address(self, value: str) -> None:
        """
        Вводит адрес в форму.

        :param value: Адрес для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='address']").send_keys(value)

    @allure.step("Ввод email: {value}")
    def email(self, value: str) -> None:
        """
        Вводит email в форму.

        :param value: Email для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='e-mail']").send_keys(value)

    @allure.step("Ввод телефона: {value}")
    def phone(self, value: str) -> None:
        """
        Вводит телефон в форму.

        :param value: Телефон для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='phone']").send_keys(value)

    @allure.step("Ввод почтового индекса: {value}")
    def zip_code(self, value: str) -> None:
        """
        Вводит почтовый индекс в форму.

        :param value: Почтовый индекс для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='zip-code']").send_keys(value)

    @allure.step("Ввод города: {value}")
    def city(self, value: str) -> None:
        """
        Вводит город в форму.

        :param value: Город для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='city']").send_keys(value)

    @allure.step("Ввод страны: {value}")
    def country(self, value: str) -> None:
        """
        Вводит страну в форму.

        :param value: Страна для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='country']").send_keys(value)

    @allure.step("Ввод должности: {value}")
    def job_position(self, value: str) -> None:
        """
        Вводит должность в форму.

        :param value: Должность для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='job-position']").send_keys(value)

    @allure.step("Ввод компании: {value}")
    def company(self, value: str) -> None:
        """
        Вводит компанию в форму.

        :param value: Компания для ввода.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "input.form-control[name='company']").send_keys(value)

    @allure.step("Отправка формы")
    def send_form(self) -> None:
        """
        Отправляет форму.

        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()