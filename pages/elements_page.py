import base64
import os
import time
import random

import requests

from locators.elements_page_locators import TextBoxPageLocators as locators
from locators.elements_page_locators import *
from generator.generator import generated_file, generated_person
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
    
    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        
        return str(age)
    
    def delete_person(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()
        time.sleep(1)

    def check_delete(self):
        return self.element_is_present(self.locators.NO_RAWS_ELEMENT).text
    
    def select_up_to_some_rows(self):
        count = [5, 10, 20, 25]
        data = []
        for x in count:
            select_row_number = self.element_is_visible(self.locators.SELECT_ROW_NUMBER)
            self.go_to_element(select_row_number)
            select_row_number.click()
            self.element_is_visible((By.CSS_SELECTOR,f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())

        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)

class ButtonPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ButtonPageLocators()

    def click_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.element_is_present(self.locators.DOUBLE_CLICK_RESULT).text

        elif type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_BUTTON))
            return self.element_is_present(self.locators.RIGHT_CLICK_RESULT).text 

        elif type_click == "click":
            self.element_is_visible(self.locators.CLICK_BUTTON).click()
            return self.element_is_present(self.locators.CLICK_RESULT).text
        
class LinksPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code
        
    def check_broken_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST).click
        else:
            return request.status_code
        
class UploadDownloadPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = UploadDownloadPageLocators()

    def upload_file(self):
        file_content = f'Hello World {random.randint(1, 999)}'
        path = generated_file("txt", file_content, "w+")
        self.element_is_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_is_present(self.locators.UPLOADED_FILE).text.split('\\')[-1]
        file_name = path.split('/')[-1]
        return file_name, text
    
    def download_file(self):
        link = self.element_is_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        offset = link_b.find(b'\xff\xd8')
        path_name_file = generated_file("jpg", link_b[offset:], "wb+")
        check_file = os.path.exists(path_name_file)
        os.remove(path_name_file)
        return check_file
    
class DynamicPropertiesPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DynamicPropertiesPageLocators()

    def check_change_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_after
    
    def check_appear_button(self):
        time.sleep(5)
        visible_button = self.element_is_visible(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        return visible_button
    
    def check_enable_button(self):
        time.sleep(5)
        return self.element_is_clickable(self.locators.ENABLE_BUTTON)
   
        

    






















    









