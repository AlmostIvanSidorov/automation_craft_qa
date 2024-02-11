import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from generator.generator import generated_color, generated_date
from locators.interactions_locators import *
from selenium.common.exceptions import *
from pages.base_page import BasePage
import re

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
    
class ResizablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ResizablePageLocators()

    def __get_sizes(self, element):
        size = self.element_is_present(element).get_attribute('style')
        width = size.split(";")[0].split(":")[1].replace(' ', '')
        height = size.split(";")[1].split(":")[1].replace(' ', '')

        return width, height
    
    def __change_sizes(self, element, handle, width, height):
        self.action_drag_and_drop_by_offset(self.element_is_present(handle), width, height)
        changed_size = self.__get_sizes(element)
        return changed_size
    
    def get_min_max_size_resizable_box(self):
        max_size = self.__change_sizes(self.locators.RESIZABLE_BOX, self.locators.RESIZABLE_BOX_HANDLE, 400, 200)
        time.sleep(1)
        min_size = self.__change_sizes(self.locators.RESIZABLE_BOX, self.locators.RESIZABLE_BOX_HANDLE, -500, -300)

        return min_size, max_size
    
    def get_min_max_size_resizable(self):
        max_size = self.__change_sizes(self.locators.RESIZABLE, self.locators.RESIZABLE_HANDLE, random.randint(1,30), random.randint(1,30))
        time.sleep(1)
        min_size = self.__change_sizes(self.locators.RESIZABLE, self.locators.RESIZABLE_HANDLE, random.randint(-20,-1), random.randint(-20,-1))

        return min_size, max_size
    

class DroppablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DroppablePageLocators()

    def drop_simple(self):
        self.element_is_visible(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)


        self.action_drag_and_drop_by_element(drag_div,drop_div)

        return drop_div.text
    
    def drop_accept(self):
        self.element_is_visible(self.locators.ACCEPT_TAB).click()

        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)

        
        self.action_drag_and_drop_by_element(not_acceptable_div,drop_div)
        drop_text_not_accept = drop_div.text
        self.action_drag_and_drop_by_element(acceptable_div,drop_div)
        drop_text_accept = drop_div.text

        return drop_text_not_accept, drop_text_accept
    
    def drop_prevent_propogation(self):
        self.element_is_visible(self.locators.PREVENT_TAB).click()

        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_inner_box = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_inner_box = self.element_is_visible(self.locators.GREEDY_INNER_BOX)
        self.action_drag_and_drop_by_element(drag_div, not_greedy_inner_box)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_inner_box = not_greedy_inner_box.text
        self.action_drag_and_drop_by_element(drag_div, greedy_inner_box)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_inner_box = greedy_inner_box.text

        return text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box
    
    def __drop_revert_not_revert_draggable(self, revert_locator):
        self.element_is_clickable(self.locators.REVERT_TAB).click()
        revert = self.element_is_clickable(revert_locator)
        drop_div = self.element_is_clickable(self.locators.DROP_HERE_REVERT)
        self.action_drag_and_drop_by_element(revert,drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')

        return position_after_move, position_after_revert
    
    def drop_will_revert_draggable(self):
        return self.__drop_revert_not_revert_draggable(self.locators.WILL_REVERT)

    def drop_will_not_revert_draggable(self):
        return self.__drop_revert_not_revert_draggable(self.locators.NOT_REVERT)
    
class DraggablePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DraggablePageLocators()

    def get_before_and_after_position(self, drag_element):
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0,50), random.randint(0,50))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0,50), random.randint(0,50))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    def simple_drag_box(self):
        self.element_is_clickable(self.locators.SIMPLE_TAB).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME)
        return self.get_before_and_after_position(drag_div)
    
    def get_top_position(self, positions):
        return re.findall(r'\d+', positions.split(';')[2]) #https://regex101.com/

    def get_left_position(self, positions):
        return re.findall(r'\d+', positions.split(';')[1])

    def axis_restricted_x(self):
        self.element_is_clickable(self.locators.AXIS_TAB).click()
        only_x = self.element_is_visible(self.locators.ONLY_X)
        position_x = self.get_before_and_after_position(only_x)

        top_x_before = self.get_top_position(position_x[0]) 
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1]) 
        return [top_x_before, top_x_after],[left_x_before,left_x_after]
    
    def axis_restricted_y(self):
        self.element_is_clickable(self.locators.AXIS_TAB).click()
        only_y = self.element_is_visible(self.locators.ONLY_Y)
        position_y = self.get_before_and_after_position(only_y)

        top_y_before = self.get_top_position(position_y[0]) 
        top_y_after = self.get_top_position(position_y[1])
        left_y_before = self.get_left_position(position_y[0])
        left_y_after = self.get_left_position(position_y[1]) 
        return [top_y_before, top_y_after],[left_y_before,left_y_after]





        
    

    



 


