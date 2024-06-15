from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

search_field = "#content > div > div > div > input[type=number]"

search_input = driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/input')

search_input.send_keys("1000")

sleep(2)

search_input.clear()
search_input.send_keys("999")

sleep(3)