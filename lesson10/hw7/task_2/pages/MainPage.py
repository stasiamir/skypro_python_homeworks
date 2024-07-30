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
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(3)
        self._driver.maximize_window()

    @allure.step("Установка задержки: {value}")
    def delay(self, value: str) -> None:
        """
        Устанавливает задержку на странице.

        :param value: Значение задержки для установки.
        :return: None
        """
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(value)

    @allure.step("Нажатие кнопки с текстом: {text}")
    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку с заданным текстом.

        :param text: Текст на кнопке для нажатия.
        :return: None
        """
        self._driver.find_element(By.XPATH, f"//span[text() = '{text}']").click()