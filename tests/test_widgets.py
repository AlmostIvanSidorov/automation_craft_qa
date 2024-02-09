import time
import pytest

from pages.widgets_page import *

class TestWidgets:
    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open()
            headers = ['first', 'second', 'third']
            content = []
            for header in headers:
                content.append(accordian_page.check_accordian(header))

            assert content[0] == ['What is Lorem Ipsum?', 574], "some problems with 1 paragraph"
            assert content[1][0] == 'Where does it come from?' and content[1][1] > 0, "some problems with 2 paragraph"
            assert content[2] == ['Why do we use it?', 613], "some problems with 3 paragraph"

    class TestAutoCompletePage:

        def test_multiple_complete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors, colors_after = autocomplete_page.fill_input_multi(3)
            assert colors == colors_after, "the added colors were missing in the input"

        def test_remove_value_from_multi(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi(3)
            colors, colors_after = autocomplete_page.remove_value_from_multi()
            assert colors != colors_after and colors == 0, "value was not deleted"

        def test_fill_single_autocomplete(self, driver):
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            color_result = autocomplete_page.check_color_in_single()
            assert color == color_result, "the added colors were missing in the input"

    class TestDatePickerPage:

        def test_change_date(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            assert value_date_before != value_date_after

        def test_change_date_and_time(self, driver):
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            date_picker_page.select_date_and_time()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before, value_date_after)
            assert value_date_before != value_date_after


            


            

