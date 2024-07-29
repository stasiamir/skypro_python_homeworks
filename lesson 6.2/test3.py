from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_online_shop():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    # Переход на веб-страницу
    driver.get("https://www.saucedemo.com/")

    # ввод username
    username_locator = '#user-name'
    input_username = driver.find_element(By.CSS_SELECTOR, username_locator)
    input_username.send_keys("standard_user")

    # ввод password
    password_locator = '#password'
    input_password = driver.find_element(By.CSS_SELECTOR, password_locator)
    input_password.send_keys("secret_sauce")

    # Нажатие кнопки Login
    button_locator = '#login-button'
    driver.find_element(By.CSS_SELECTOR, button_locator).click()

    # Добавление товара Sauce Labs Backpack
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

    # Добавление товара Sauce Labs Bolt T-Shirt
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Добавление товара Sauce Labs Onesie
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container>a').click()

    # Нажатие кнопки Checkout
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    # Ввод FirstName
    first_name_locator = '#first-name'
    input_first_name = driver.find_element(By.CSS_SELECTOR, first_name_locator)
    input_first_name.send_keys("Виктория")

    # Ввод LastName
    last_name_locator = '#last-name'
    input_last_name = driver.find_element(By.CSS_SELECTOR, last_name_locator)
    input_last_name.send_keys("Ситникова")

    # Ввод Zip/PostalCode
    postal_code_locator = '#postal-code'
    input_postal_code = driver.find_element(
        By.CSS_SELECTOR, postal_code_locator)
    input_postal_code.send_keys("9000")

    # Нажатие кнопки Continue
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    # Получение итоговой стоимости и сохранение её в переменную
    text_result = driver.find_element(
        By.XPATH, "//*[@id='checkout_summary_container']/div/div[2]/div[8]").text

    driver.quit()

    # Проверка результата
    assert text_result == "Total: $58.29"