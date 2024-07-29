import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу с результатами.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Ожидание и получение результата времени")
    def display_time_result(self) -> int:
        """
        Ожидает, пока результат времени будет отображен, и возвращает его.

        :return: Результат времени в виде целого числа.
        :rtype: int
        """
        waiter = WebDriverWait(self._driver, 46)
        waiter.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

        result_element = self._driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div')
        return int(result_element.text)