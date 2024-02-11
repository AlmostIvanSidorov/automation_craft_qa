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

