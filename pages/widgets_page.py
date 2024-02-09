import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from generator.generator import generated_color, generated_date
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
    
class DatePickerPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DatePickerLocators()

    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR,date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')

        return value_date_before, value_date_after
    
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        time.sleep(1)
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_YEAR_LIST, '2020')
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_TIME_LIST, date.time)
        time.sleep(1)
        value_date_after = input_date.get_attribute('value')

        return value_date_before, value_date_after


    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1,100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_after, value_before



class ProgressBarPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ProgressBarPageLocators()

    def change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        # value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_clickable(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1,10))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).get_attribute('aria-valuenow')
        # value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_after, value_before
    

class TabsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = TabsPageLocators()

    def check_tabs(self, name_tab):
        button = self.element_is_visible(self.locators.tabs[name_tab]['button'])
        button.click()
        content = self.element_is_visible(self.locators.tabs[name_tab]['content']).text
        return [button.text, len(content)]
        

