import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("-headless")
    driver_service = chromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
