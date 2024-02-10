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

    class TestSliderPage:
        def test_slider(self, driver):
            slider = SliderPage(driver, 'https://demoqa.com/slider')
            slider.open()
            after, before = slider.change_slider_value()
            assert before < after , "slider doesn't move correct"

    class TestProgressBarPage:
        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open()
            after, before = progress_bar.change_progress_bar_value()
            assert before < after , "progress bar doesn't work correct"


    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, "https://demoqa.com/tabs")
            tabs.open()
            tabs_list = ['What', 'Origin', 'Use', 'More']

            for tab_name in tabs_list:
                tab = tabs.check_tabs(tab_name)
                assert tab[0] == tab_name and tab[1] != 0, f"The tab {tab_name} was not pressed or the text is missing."


    class TestToolTipsPage:

        def test_tool_tips(self, driver):
            tool_tips_page = ToolTipsPage(driver, "https://demoqa.com/tool-tips")
            tool_tips_page.open()
            text_button, text_field, text_contrary, text_section = tool_tips_page.check_tool_tips()

            assert text_button == 'You hovered over the Button', 'hover missing or incorrect content'
            assert text_field == 'You hovered over the text field', 'hover missing or incorrect content'
            assert text_contrary == 'You hovered over the Contrary', 'hover missing or incorrect content'
            assert text_section == 'You hovered over the 1.10.32', 'hover missing or incorrect content'


    class TestMenuPage:

        def test_menu(self, driver):
            menu_page = MenuPage(driver, "https://demoqa.com/menu")
            menu_page.open()
            data = menu_page.check_menu()
            assert data == ['Main Item 1', 'Main Item 2\nSub Item\nSub Item\nSUB SUB LIST »',
                             'Sub Item', 'Sub Item', 'SUB SUB LIST »\nSub Sub Item 1\nSub Sub Item 2',
                               'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], "menu items doesn't exist or have not been found"


            





            


            

