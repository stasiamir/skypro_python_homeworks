from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_calculator():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
    # Переход на веб-страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # В поле ввода по локатору #delay вводим значение 45.
    delay_locator = "#delay"
    input_delay = driver.find_element(By.CSS_SELECTOR, delay_locator)
    input_delay.clear()
    input_delay.send_keys("45")

    # Нажатие на кнопку 7
    seven_name_locator = '//*[@id="calculator"]/div[2]/span[1]'
    driver.find_element(By.XPATH, seven_name_locator).click()

    # Нажатие на кнопку +
    plus_name_locator = '//*[@id="calculator"]/div[2]/span[4]'
    driver.find_element(By.XPATH, plus_name_locator).click()

    # Нажатие на кнопку 8
    eight_name_locator = '//*[@id="calculator"]/div[2]/span[2]'
    driver.find_element(By.XPATH, eight_name_locator).click()

    # Нажатие на кнопку =
    equals_name_locator = '//*[@id="calculator"]/div[2]/span[15]'
    driver.find_element(By.XPATH, equals_name_locator).click()

    result_locator = '//*[@id="calculator"]/div[1]/div'
    waiter = WebDriverWait(driver, 46)
    result = waiter.until(EC.text_to_be_present_in_element(
        (By.XPATH, result_locator), "15"))

    # Проверка результата
    assert result, "The result is not as expected"

    driver.quit()