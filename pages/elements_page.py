import time
import random

from locators.elements_page_locators import TextBoxPageLocators as locators
from locators.elements_page_locators import CheckBoxPageLocators
from generator.generator import generated_person
from pages.base_page import BasePage

class TextBoxPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def fill_all_fields(self):
        person_info = next(generated_person())
        input_full_name = person_info.full_name
        input_email = person_info.email
        input_current_address = person_info.current_address
        input_permanent_address = person_info.permanent_address
        self.element_is_visible(locators.FULL_NAME).send_keys(input_full_name)
        self.element_is_visible(locators.EMAIL).send_keys(input_email)
        self.element_is_visible(locators.CURRENT_ADDRESS).send_keys(input_current_address)
        self.element_is_visible(locators.PERMANENT_ADDRESS).send_keys(input_permanent_address)
        self.element_is_visible(locators.SUBMIT_BUTTON).click()

        time.sleep(2)

        return input_full_name, input_email, input_current_address, input_permanent_address

    def check_field_form(self):
        full_name = self.element_is_present(locators.CREATED_FULL_NAME).text.split(":")[1]
        email = self.element_is_present(locators.CREATED_EMAIL).text.split(":")[1]
        current_address = self.element_is_present(locators.CREATED_CURRENT_ADDRESS).text.split(":")[1]
        permanent_address = self.element_is_present(locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1]

        return full_name, email, current_address, permanent_address
    
class CheckBoxPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)

        count = 21

        while count != 0:
            item = item_list[random.randint(1,15)]
            self.go_to_element(item)
            item.click()
            count -= 1

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_BOXES_LOCATOR)
        data = [] 
        for box in checked_list:
            data.append(box.find_element("xpath", self.locators.TITLE_ITEM).text.replace(' ', '').replace(".doc", "").lower().replace("file","File"))

        return data
    
    def return_result(self):
        result_text_list = []

        result_list = self.elements_are_present(self.locators.EXPECTED_RESULT_LOCATOR)
        for item in result_list:
            result_text_list.append(item.text)

        return result_text_list

class RadioButtonPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = CheckBoxPageLocators()



