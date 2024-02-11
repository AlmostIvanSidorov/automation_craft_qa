import time
import pytest

from pages.interactions_page import *

class TestInteractions:
    class TestSortablePage:

        def test_sortable_list(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_order()
            assert order_before != order_after, "the order of the list has not been changed"

        def test_sortable_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_grid_order()
            assert order_before != order_after, "the order of the grid has not been changed"

            
    class TestSelectablePage:

        def test_selectable_list(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            chosen_element, selected_element = selectable_page.select_list_item()
            assert chosen_element == selected_element, "element was not clicked"

        def test_selectable_grid(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            chosen_element, selected_element = selectable_page.select_grid_item()
            assert chosen_element == selected_element, "element was not clicked"

    class TestResizablePage:
        def test_resizable(self,driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            min_sizes, max_sizes = resizable_page.get_min_max_size_resizable()
            assert min_sizes != max_sizes, "resizable box has not been changed"

        def test_resizable_box(self,driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            min_sizes, max_sizes = resizable_page.get_min_max_size_resizable_box()
            assert min_sizes == ('150px', '150px'), "minimum size is not equal to '150px', '150px'"
            assert max_sizes == ('500px', '300px'), "maximum size is not equal to '500px', '300px'"

    class TestDroppablePage:
         
         def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "the element has not been dropped" 

         def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            drop_text_not_accept, drop_text_accept = droppable_page.drop_accept()
            assert drop_text_not_accept == "Drop here", "wrong element has been dropped"

            assert drop_text_accept == "Dropped!", "the element has not been dropped"

         def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_not_greedy_box, text_not_greedy_inner_box, text_greedy_box, text_greedy_inner_box = droppable_page.drop_prevent_propogation()
            time.sleep(1)
            assert text_not_greedy_box == "Dropped!", "the elements text has not been changed"
            assert text_not_greedy_inner_box == "Dropped!", "the elements text has not been changed"
            assert text_greedy_box == "Outer droppable", "the elements text has been changed"
            assert text_greedy_inner_box == "Dropped!", "the elements text has not been changed"


         def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            position_after_move, position_after_revert = droppable_page.drop_will_revert_draggable()

            assert position_after_move != position_after_revert, "element doesn't revert"

            position_after_move, position_after_revert = droppable_page.drop_will_not_revert_draggable()
            assert position_after_move == position_after_revert, "element revert"




             

