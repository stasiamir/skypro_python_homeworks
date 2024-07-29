import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу результатов.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Получение текста результата")
    def text_result(self) -> str:
        """
        Получает текст результата со страницы.

        :return: Текст результата в виде строки.
        :rtype: str
        """
        txt = self._driver.find_element(By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text
        return txt