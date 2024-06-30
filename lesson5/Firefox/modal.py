from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

search_input = driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p')

sleep(2)

search_input.click()

sleep(3)