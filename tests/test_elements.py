from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_textbox(self, driver):
            textbox_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            textbox_page.open()
            input_full_name, input_email, input_current_address, input_permanent_address = textbox_page.fill_all_fields()

            output_full_name, output_email, output_current_address, output_permanent_address = textbox_page.check_field_form()

            assert output_full_name == input_full_name, "the full name doesn't match"
            assert output_email == input_email, "the email doesn't match"
            assert output_current_address == input_current_address, "the current address doesn't match"
            assert output_permanent_address == input_permanent_address, "the permanent address doesn't match"
            
