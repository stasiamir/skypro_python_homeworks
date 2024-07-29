from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    result = WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"))).text
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"