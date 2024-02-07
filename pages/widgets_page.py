import random
import time
from selenium.webdriver import Keys
from generator.generator import generated_color
from locators.widgets_locators import *
from selenium.common.exceptions import *
from pages.base_page import BasePage


class AccordianPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = AccordianLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first': 
                        {'title': self.locators.SECTION_FIRST,
                         'content': self.locators.SECTION_CONTENT_FIRST},
                     'second': 
                        {'title': self.locators.SECTION_SECOND,
                         'content': self.locators.SECTION_CONTENT_SECOND},
                     'third': 
                        {'title': self.locators.SECTION_THIRD,
                         'content': self.locators.SECTION_CONTENT_THIRD},}
        
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]
    
class AutoCompletePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = AutoCompleteLocators()

    def fill_input_multi(self, insert_number = None):
        if insert_number == None:
            insert_number = 1
        color = generated_color()
        input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
        print(color)
        # for i in range(insert_number):
        #     input_multi.send_keys(color)
        #     input_multi.send_keys(Keys.ENTER)


    

