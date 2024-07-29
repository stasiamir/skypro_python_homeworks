from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage: 
    
    
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.maximize_window()
        
    def set_delay(self, num):
        delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(num)
    
    def sum_function(self, num1, num2):
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num1}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH, f"//span[contains(text(),'{num2}')]").click()
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click()
       

    def result_sum(self, to_be, delay):
        waiter = WebDriverWait(self._driver, delay + 1)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div[class='screen']"), str(to_be))
        )
        res_sum = self._driver.find_element(By.CSS_SELECTOR, "div[class='screen']").get_attribute("innerText")
        return int(res_sum)