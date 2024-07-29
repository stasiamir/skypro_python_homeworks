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


@allure.title("Проверка красного элемента для пустого почтового индекса")
@allure.description("Этот тест проверяет, что результат с пустым почтовым индексом отображается красным цветом.")
@allure.feature("Валидация форм")
@allure.severity(allure.severity_level.CRITICAL)
def test_red_element():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)

    with allure.step("Заполнение формы"):
        main_page.first_name("Иван")
        main_page.last_name("Петров")
        main_page.address("Ленина, 55-3")
        main_page.email("test@skypro.com")
        main_page.phone("+7985899998787")
        main_page.zip_code("")
        main_page.city("Москва")
        main_page.country("Россия")
        main_page.job_position("QA")
        main_page.company("SkyPro")

    with allure.step("Отправка формы"):
        main_page.send_form()

    result_page = ResultPage(browser)

    with allure.step("Проверка результата"):
        to_be = result_page.empty_zip_result_is_red()
        as_is = 1
        assert as_is == to_be, "Элемент с пустым почтовым индексом не отображается красным цветом"

    with allure.step("Закрытие браузера"):
        browser.quit()


@allure.title("Проверка зеленых элементов")
@allure.description("Этот тест проверяет, что остальные элементы результатов отображаются зеленым цветом.")
@allure.feature("Валидация форм")
@allure.severity(allure.severity_level.NORMAL)
def test_green_elements():
    with allure.step("Открытие браузера"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(browser)

    with allure.step("Заполнение формы"):
        main_page.first_name("Иван")
        main_page.last_name("Петров")
        main_page.address("Ленина, 55-3")
        main_page.email("test@skypro.com")
        main_page.phone("+7985899998787")
        main_page.zip_code("")
        main_page.city("Москва")
        main_page.country("Россия")
        main_page.job_position("QA")
        main_page.company("SkyPro")

    with allure.step("Отправка формы"):
        main_page.send_form()

    result_page = ResultPage(browser)

    with allure.step("Проверка результата"):
        classes = result_page.other_elements_result_is_green()
        assert 'alert-success' in classes, "Другие элементы результатов не отображаются зеленым цветом"

    with allure.step("Закрытие браузера"):
        browser.quit()