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

        colors_after = []

        colors = generated_color(insert_number)
        input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
        for color in colors:
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)

        for element in self.elements_are_visible(self.locators.MULTI_VALUE):
            colors_after.append(element.text)

        return colors, colors_after

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()

        try:
            count_value_after = len(self.elements_are_visible(self.locators.MULTI_VALUE))
        except TimeoutException:
            count_value_after = 0

        return count_value_after, count_value_before
    
    def fill_input_single(self):
        color = generated_color(1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]
    
    def  check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text

