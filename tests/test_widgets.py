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
            autocomplete_page.fill_input_multi(2)
            time.sleep(4)


            

