import time
import pytest

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

            assert key_word in found_person

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_persons(count=1)[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()

            assert age in row, "raw with new age was not found"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_persons(count=1)[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            
            assert text == 'No rows found', "row was not deleted"

        @pytest.mark.xfail(reason="doesn't see option window")
        def test_web_table_change_row_number(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()

            assert count == [5, 10, 20, 25], "row number was not change correct"

    class TestButtonPage:

        def test_different_clicks_on_buttons(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()

            double = button_page.click_different_button("double")

            right = button_page.click_different_button("right")

            click = button_page.click_different_button("click")

            assert double == "You have done a double click", "You have not done a double click"
            assert right == "You have done a right click", "You have not done a right click"
            assert click == "You have done a dynamic click", "You have not done a dynamic click"

    class TestLinksPage:

        def test_check_link(self,driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_simple_link()
            assert link_href == current_url, "the link is broken or url is incorrect"

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400, "status code is not 400"

    class TestUploadDownloadPage:

        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result

        def test_download_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()





            
