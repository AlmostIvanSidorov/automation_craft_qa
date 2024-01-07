import time

from pages.elements_page import *

class TestElements:
    class TestTextBox:
        def test_elements(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = text_box_page.fill_all_fields()

            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()

            assert output_full_name == input_full_name, "the full name doesn't match"
            assert output_email == input_email, "the email doesn't match"
            assert output_current_address == input_current_address, "the current address doesn't match"
            assert output_permanent_address == input_permanent_address, "the permanent address doesn't match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()

            output_result = check_box_page.return_result()
            assert input_checkboxes == output_result, "marked checkboxes are not equal to shown checkboxes "

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()

            time.sleep(3)

            
