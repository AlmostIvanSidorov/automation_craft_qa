import time
import random

from locators.elements_page_locators import TextBoxPageLocators as locators
from locators.elements_page_locators import *
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

    locators = RadioButtonPageLocators()

    def click_random_button(self):
        buttons_list = self.elements_are_visible(self.locators.RADIO_BUTTONS)

        clicked_button = buttons_list[random.randint(0,2)]

        clicked_button.click()

        return clicked_button.text
    
    def selected_button(self):
        return self.element_is_visible(self.locators.SELECTED_BUTTON).text
    
class WebTablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = WebTablePageLocators()

    def add_new_persons(self, count=None):
        if count is None:
            count = random.randint(1,10)

        while count != 0:

            self.element_is_visible(self.locators.ADD_BUTTON).click()

            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)

            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1


        return [firstname, lastname, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())

        return data
    
    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element("xpath", self.locators.RAW_PARENT)

        return row.text.splitlines()




    









