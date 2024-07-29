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
from pages.AuthorizationPage import AuthorizationPage
from pages.InformationPage import InformationPage
from pages.CartPage import CartPage


@allure.title("Проверка итоговой суммы после оформления заказа")
@allure.description("Этот тест проверяет, что итоговая сумма заказа составляет $58.29.")
@allure.feature("Оформление заказа")
@allure.severity(allure.severity_level.CRITICAL)
def test_result():
    with allure.step("Открытие браузера и переход на страницу авторизации"):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        authorization_page = AuthorizationPage(browser)

    with allure.step("Ввод учетных данных и вход в систему"):
        authorization_page.username("standard_user")
        authorization_page.password("secret_sauce")
        authorization_page.click_login()

    main_page = MainPage(browser)

    with allure.step("Добавление товаров в корзину"):
        main_page.add_to_cart()

    cart_page = CartPage(browser)

    with allure.step("Переход в корзину и к оформлению заказа"):
        cart_page.get_to_cart()
        cart_page.get_to_checkout()

    information_page = InformationPage(browser)

    with allure.step("Ввод информации для оформления заказа"):
        information_page.add_first_name("Виктория")
        information_page.add_last_name("Ситникова")
        information_page.add_zip_code("0000")
        information_page.click_button()

    result_page = ResultPage(browser)

    with allure.step("Получение итоговой суммы"):
        result_amount = result_page.text_result()

    with allure.step("Закрытие браузера"):
        browser.quit()

    with allure.step("Проверка итоговой суммы"):
        assert result_amount == "Total: $58.29", f"Ожидалось 'Total: $58.29', но получено '{result_amount}'"