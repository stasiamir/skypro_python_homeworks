from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
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

sleep(3)