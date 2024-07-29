import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage


@allure.title("Проверка результата калькуляции")
@allure.description("Этот тест проверяет, что результат калькуляции после задержки составляет 15.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_result():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)

    with allure.step("Установка задержки"):
        main_page.delay("45")

    with allure.step("Ввод данных для калькуляции"):
        main_page.click_button("7")
        main_page.click_button("+")
        main_page.click_button("8")
        main_page.click_button("=")

    result_page = ResultPage(browser)

    with allure.step("Получение результата"):
        result = result_page.display_time_result()

    with allure.step("Проверка результата"):
        assert 15 == result, f"Expected 15, but got {result}"

    with allure.step("Закрытие браузера"):
        browser.quit()