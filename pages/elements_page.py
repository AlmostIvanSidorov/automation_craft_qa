import time

from locators.elements_page_locators import TextBoxPageLocators as locators
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    input_full_name = "admin"
    input_email = "admin@email.com"
    input_current_address = "some street"
    input_permanent_address = "same street"

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def fill_all_fields(self):
        self.element_is_visible(locators.FULL_NAME).send_keys(self.input_full_name)
        self.element_is_visible(locators.EMAIL).send_keys(self.input_email)
        self.element_is_visible(locators.CURRENT_ADDRESS).send_keys(self.input_current_address)
        self.element_is_visible(locators.PERMANENT_ADDRESS).send_keys(self.input_permanent_address)
        self.element_is_visible(locators.SUBMIT_BUTTON).click()

        time.sleep(2)

    def check_field_form(self):
        full_name = self.element_is_present(locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]

        return full_name, email, current_address, permanent_address

