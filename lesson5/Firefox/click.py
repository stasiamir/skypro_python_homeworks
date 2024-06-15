from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

search_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

search_input.click()
search_input.click()
search_input.click()
search_input.click()
search_input.click()

button_delete = driver.find_elements(By.XPATH, '//*[@id="elements"]/button')

print(len(button_delete))