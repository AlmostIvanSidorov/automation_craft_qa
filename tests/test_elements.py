import time
import pytest
import allure

from pages.elements_page import *

@allure.suite("Elements")
class TestElements:

    @allure.feature('TextBox')
    class TestTextBox:

        @allure.title('Check TextBox')
        def test_elements(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = text_box_page.fill_all_fields()

            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()

            assert output_full_name == input_full_name, "the full name doesn't match"
            assert output_email == input_email, "the email doesn't match"
            assert output_current_address == input_current_address, "the current address doesn't match"
            assert output_permanent_address == input_permanent_address, "the permanent address doesn't match"

    @allure.feature('CheckBox')
    class TestCheckBox:

        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, "https://demoqa.com/checkbox")
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkboxes = check_box_page.get_checked_checkboxes()

            output_result = check_box_page.return_result()
            assert input_checkboxes == output_result, "marked checkboxes are not equal to shown checkboxes "

    @allure.feature('RadioButton')
    class TestRadioButton:
        
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
            radio_button_page.open()
            input_radio_button = radio_button_page.click_random_button()
            output_radio_button = radio_button_page.selected_button()

            assert input_radio_button == output_radio_button, "Radio button click works incorrect"


            time.sleep(3)

    @allure.title('WebTable')
    class TestWebTable:


        @allure.title('Check WebTable_1')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            new_person = web_table_page.add_new_persons(count=1)
            table_result = web_table_page.check_new_added_person()

            assert new_person in table_result

        @allure.title('Check WebTable_2')
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

        @allure.title('Check WebTable_3')
        def test_web_table_search_persons(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            key_word = web_table_page.add_new_persons(count=1)[random.randint(0,5)]
            web_table_page.search_some_person(key_word)
            found_person = web_table_page.check_search_person()

            assert key_word in found_person

        @allure.title('Check WebTable_5')
        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            lastname = web_table_page.add_new_persons(count=1)[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()

            assert age in row, "raw with new age was not found"

        @allure.title('Check WebTable_6')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_persons(count=1)[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_person()
            text = web_table_page.check_delete()
            
            assert text == 'No rows found', "row was not deleted"

        @allure.title('Check WebTable_7')
        @pytest.mark.xfail(reason="doesn't see option window")
        def test_web_table_change_row_number(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_up_to_some_rows()

            assert count == [5, 10, 20, 25], "row number was not change correct"

    @allure.feature('Check ButtonPage')
    class TestButtonPage:

        @allure.title('Check ButtonPage_1')
        def test_different_clicks_on_buttons(self, driver):
            button_page = ButtonPage(driver, 'https://demoqa.com/buttons')
            button_page.open()

            double = button_page.click_different_button("double")

            right = button_page.click_different_button("right")

            click = button_page.click_different_button("click")

            assert double == "You have done a double click", "You have not done a double click"
            assert right == "You have done a right click", "You have not done a right click"
            assert click == "You have done a dynamic click", "You have not done a dynamic click"

    @allure.feature('Check LinksPage')
    class TestLinksPage:

        @allure.title('Check LinksPage_1')
        def test_check_link(self,driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_simple_link()
            assert link_href == current_url, "the link is broken or url is incorrect"

        @allure.title('Check LinksPage_2')
        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link("https://demoqa.com/bad-request")
            assert response_code == 400, "status code is not 400"

    @allure.feature('Check UploadDownloadPage')
    class TestUploadDownloadPage:

        @allure.title('Check UploadDownloadPage_1')
        def test_upload_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "the file has not been uploaded"

        @allure.title('Check UploadDownloadPage_2')
        def test_download_file(self, driver):
            upload_download_page = UploadDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            check = upload_download_page.download_file()
            assert check is True,"the file has not been downloaded"

    @allure.feature('Check DynamicProperties')
    class TestDynamicProperties:

        @allure.title('Check DynamicProperties_1')
        def test_color_button(self,driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_button_after = dynamic_properties_page.check_change_of_color()
            assert str(color_button_after) == 'rgba(220, 53, 69, 1)', "button did not change color after 5 sec"

        @allure.title('Check DynamicProperties_2')
        def test_check_appear_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            appear_button = dynamic_properties_page.check_appear_button()
            assert appear_button.text == "Visible After 5 Seconds", "button did not appear color after 5 sec"

        @allure.title('Check DynamicProperties_3')
        def test_check_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            enable_button = dynamic_properties_page.check_enable_button()
            assert enable_button is not None, "button did not become clickable color after 5 sec"






    

    







            
