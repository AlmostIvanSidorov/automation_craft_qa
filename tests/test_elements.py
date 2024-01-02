from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_elements(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            text_box_page.fill_all_fields()

            output_full_name, output_email, output_current_address, output_permanent_address = text_box_page.check_field_form()

            assert output_full_name == text_box_page.input_full_name, "wrong full name"
            assert output_email == text_box_page.input_email, "wrong email"
            assert output_current_address == text_box_page.input_current_address, "wrong current address"
            assert output_permanent_address == text_box_page.input_permanent_address, "wrong permanent address"
            
