from selenium import webdriver
from form.FormPage import FormPage
import pytest


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')


values_dict = {'first-name': 'Иван', 'last-name': 'Петров', 'address': 'Ленина, 55-3',
               'e-mail': 'test@skypro.com', 'city': 'Москва', 'country': 'Россия',
               'job-position': 'QA', 'phone': '+7985899998787', 'company': 'SkyPro', 'zip-code': ''}

alert_danger_color = "rgba(248, 215, 218, 1)"
alert_success_color = "rgba(209, 231, 221, 1)"

fields_to_test_success = [key for key in values_dict.keys() if key != 'zip-code']


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()


@pytest.fixture(scope="module")
def setup_form(browser):
    form_page = FormPage(browser)
    form_page.open()
    form_page.fill_fields(values_dict)
    form_page.click_submit()
    return form_page


def test_alert_color(setup_form):
    color_zip = setup_form.find_element_property("zip-code")
    assert color_zip == alert_danger_color


@pytest.mark.parametrize('selector', fields_to_test_success)
def test_success_color(setup_form, selector):
    color = setup_form.find_element_property(selector)
    assert color == alert_success_color