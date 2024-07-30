import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализирует страницу с результатами.

        :param driver: Экземпляр WebDriver для взаимодействия с браузером.
        """
        self._driver = driver

    @allure.step("Проверка, что результат с пустым почтовым индексом имеет красный цвет")
    def empty_zip_result_is_red(self) -> int:
        """
        Проверяет, что результат с пустым почтовым индексом помечен красным цветом.

        :return: Количество элементов с пустым почтовым индексом, имеющих красный цвет.
        :rtype: int
        """
        zip_id = self._driver.find_elements(By.CSS_SELECTOR, "#zip-code.alert-danger")
        return len(zip_id)

    @allure.step("Проверка, что другие элементы результатов имеют зеленый цвет")
    def other_elements_result_is_green(self) -> list:
        """
        Проверяет, что другие элементы результатов имеют зеленый цвет.

        :return: Список классов элементов, исключая элемент с ID 'zip-code'.
        :rtype: list
        """
        elements = self._driver.find_elements(By.CSS_SELECTOR, "div.alert")
        for el in elements:
            id_element = el.get_attribute('id')
            # пропуск элемента zip-code
            if id_element == 'zip-code':
                continue
            class_list = el.get_attribute("class").split(' ')
            return class_list