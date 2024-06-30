import pytest
from selenium import webdriver

from calculator.CalcPage import CalcPage


@pytest.mark.test_calculator
def test_sum():
    browser = webdriver.Chrome()
    d = 45
    to_be = 15
    calc= CalcPage(browser)
    calc.set_delay(d)
    calc.sum_function(7, 8)
    as_is = calc.result_sum(to_be, d)
    assert as_is == to_be
    
    browser.quit()