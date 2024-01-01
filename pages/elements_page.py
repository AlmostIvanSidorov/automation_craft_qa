import time

from locators.elements_page_locators import TextBoxPageLocators as locators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def fill_all_fields(self):
        self.element_is_visible(locators.FULL_NAME).send_keys("admin")
        self.element_is_visible(locators.EMAIL).send_keys("admin@email.com")
        self.element_is_visible(locators.CURRENT_ADDRESS).send_keys("some street")
        self.element_is_visible(locators.PERMANENT_ADDRESS).send_keys("same street")
        self.element_is_visible(locators.SUBMIT_BUTTON).click()

        time.sleep(5)