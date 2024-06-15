from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

search_field = "#content > div > div > div > input[type=number]"
search_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')

search_input.send_keys("1000")

sleep(2)

search_input.clear()

search_input.send_keys("999")

sleep(3)