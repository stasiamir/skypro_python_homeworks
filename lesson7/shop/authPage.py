from selenium.webdriver.common.by import By

class AuthPage: 
    
    
    def __init__(self, driver): 
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        
    def auth(self, login, password):
        self._driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(login)
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()