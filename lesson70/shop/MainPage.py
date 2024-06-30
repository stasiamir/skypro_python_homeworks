from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser):
        self._driver = browser
        
    def add_items(self):
        waiter = WebDriverWait(self._driver,5)
        waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="app_logo"]'), "Swag Labs")
        )
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()