
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest


def test_form_submission():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Переход на веб-страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение поля имени
    first_name_locator = "input.form-control[name='first-name']"
    input_first_name = driver.find_element(By.CSS_SELECTOR, first_name_locator)
    input_first_name.send_keys("Иван")

    # Заполнение поля фамилии
    last_name_locator = "input.form-control[name='last-name']"
    input_last_name = driver.find_element(By.CSS_SELECTOR, last_name_locator)
    input_last_name.send_keys("Петров")

    # Заполнение поля адреса
    address_locator = "input.form-control[name='address']"
    input_address = driver.find_element(By.CSS_SELECTOR, address_locator)
    input_address.send_keys("Ленина, 55-3")

    # Заполнение поля электронной почты
    email_locator = "input.form-control[name='e-mail']"
    input_email = driver.find_element(By.CSS_SELECTOR, email_locator)
    input_email.send_keys("test@skypro.com")

    # Заполнение поля номера телефона
    phone_number_locator = "input.form-control[name='phone']"
    input_phone_number = driver.find_element(By.CSS_SELECTOR, phone_number_locator)
    input_phone_number.send_keys("+7985899998787")

    # Оставить поле почтового индекса пустым
    zip_code_locator = "input.form-control[name='zip-code']"
    input_zip_code = driver.find_element(By.CSS_SELECTOR, zip_code_locator)
    input_zip_code.send_keys("")

    # Заполнение поля города
    city_locator = "input.form-control[name='city']"
    input_city = driver.find_element(By.CSS_SELECTOR, city_locator)
    input_city.send_keys("Москва")

    # Заполнение поля страны
    country_locator = "input.form-control[name='country']"
    input_country = driver.find_element(By.CSS_SELECTOR, country_locator)
    input_country.send_keys("Россия")

    # Заполнение поля должности
    job_position_locator = "input.form-control[name='job-position']"
    input_job_position = driver.find_element(By.CSS_SELECTOR, job_position_locator)
    input_job_position.send_keys("QA")

    # Заполнение поля компании
    company_locator = "input.form-control[name='company']"
    input_company = driver.find_element(By.CSS_SELECTOR, company_locator)
    input_company.send_keys("SkyPro")

    # Нажатие на кнопку отправки формы
    submit_locator = "button[type=submit]"
    driver.find_element(By.CSS_SELECTOR, submit_locator).click()

    # Проверка наличия элемента zip-code с красным цветом
    zip_code_element_list = driver.find_elements(By.CSS_SELECTOR, "#zip-code.alert-danger")
    assert len(zip_code_element_list) == 1

    # Проверка наличия остальных элементов, подсвеченных зеленым
    elements = driver.find_elements(By.CSS_SELECTOR, "div.alert")
    for el in elements:
        id_element = el.get_attribute('id')
        # пропуск элемента zip-code
        if id_element == 'zip-code':
            continue

        class_list = el.get_attribute("class").split(' ')
        assert 'alert-success' in class_list

    # Закрытие браузера
    driver.quit()