import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from generator.generator import generated_color, generated_date
from locators.interactions_locators import *
from selenium.common.exceptions import *
from pages.base_page import BasePage


class SortablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SortablePageLocators()

    def __get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]
    
    def __change_order(self, tab, item):
        self.element_is_visible(tab).click()
        order_before = self.__get_sortable_items(item)
        item_list = random.sample(self.elements_are_visible(item), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_by_element(item_what, item_where)
        order_after = self.__get_sortable_items(item)

        return order_before, order_after
    
    def change_list_order(self):
        return self.__change_order(self.locators.TAB_LIST, self.locators.LIST_ITEM)
    
    def change_grid_order(self):
        return self.__change_order(self.locators.GRID_LIST, self.locators.GRID_ITEM)
    
class SelectablePage(BasePage):
   
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SelectablePageLocators()

    def __click_selectable_item(self, elements):
        item_list = self.elements_are_visible(elements)
        chosen_element = random.sample(item_list, k=1)[0]
        chosen_element.click()

        return chosen_element.text
    
    def __select_item(self, tab, item, active):
        self.element_is_visible(tab).click()
        chosen_element = self.__click_selectable_item(item)
        active_element = self.element_is_visible(active).text
        return active_element, chosen_element
    
    def select_list_item(self):
        return self.__select_item(self.locators.TAB_LIST, self.locators.LIST_ITEM, self.locators.LIST_ITEM_ACTIVE)
    
    def select_grid_item(self):
        return self.__select_item(self.locators.GRID_LIST, self.locators.GRID_ITEM, self.locators.GRID_ITEM_ACTIVE)
 

