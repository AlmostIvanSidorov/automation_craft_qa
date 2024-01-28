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
            input_radio_button = radio_button_page.click_random_button()
            output_radio_button = radio_button_page.selected_button()

            assert input_radio_button == output_radio_button, "Radio button click works incorrect"


            time.sleep(3)

    class TestWebTable:

        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_persons(count=1)
            table_result = web_table_page.check_new_added_person()

            assert new_person in table_result

        def test_web_table_add_two_persons(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            web_table_page.add_new_persons(count=2)

            table_result = web_table_page.check_new_added_person()

            number_of_not_empty_raws = 0

            for item in table_result:
                if item != ['       ']:
                    number_of_not_empty_raws += 1

            assert number_of_not_empty_raws == 5, "some persons were not added"

        def test_web_table_search_persons(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_persons(count=1)[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            found_person = web_table_page.check_search_person()
            print(found_person)
            print(key_word)

            assert key_word in found_person 







            
