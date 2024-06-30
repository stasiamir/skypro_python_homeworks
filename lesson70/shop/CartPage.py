from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, browser):
        self._driver = browser
 
    def get_cart(self):
        waiter = WebDriverWait(self._driver,5)
        self._driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
        waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="app_logo"]'), "Swag Labs")
        )
 
    def send_data(self, f_name, l_name, post_code):
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys(f_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys(l_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys(post_code)
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def total_price(self):
        txt = self._driver.find_element(
        By.CSS_SELECTOR, 'div[class="summary_total_label"]').get_attribute("textContent")
        return txt