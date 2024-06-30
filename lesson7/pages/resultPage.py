from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ResultPage:
    def __init__(self, browser):
        self._driver = browser
             
    def add_books(self):
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, "a._btn.btn-tocart.buy-link")
        counter = 0
        for btn in buy_buttons:
          btn.click()
          counter += 1
        
        return counter 
        
    def get_empty_result_message(self):
        txt = self._driver.find_element(
        By.CSS_SELECTOR, "div[class='search-error bestsellers']").find_element(By.CSS_SELECTOR, "h1").text
        return txt