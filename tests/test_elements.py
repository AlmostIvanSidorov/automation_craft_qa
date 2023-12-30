import pytest
import time

from pages.base_page import BasePage

def test(driver):
    page = BasePage(driver, 'google.com')
    page.open()
    time.sleep(3)