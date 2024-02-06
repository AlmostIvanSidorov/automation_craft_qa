import time
import pytest

from pages.alerts_frame_windows_page import *

class TestAlertsFrameWindow:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            test_result = browser_window_page.checked_opened_new_tab()
            assert test_result == 'This is a sample page', 'the new tab has not been opened or incorrect tab has been opened'

        def test_new_window(self, driver):
            browser_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            test_result = browser_window_page.checked_opened_new_window()
            assert test_result == 'This is a sample page', 'the new window has not been opened or incorrect window has been opened'

    class TestAlerts:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', "Alert didn't show up"

        def test_see_alert_after_5_sec(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', "Alert didn't show up"

        def test_confirm_box_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text = alert_page.check_alert_confirm_box()
            assert alert_text == 'You selected Ok', "Alert didn't show up"

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alert_page.open()
            alert_text, text_result = alert_page.check_prompt_alert()
            assert f'You entered {alert_text}' == text_result
            assert text_result in alert_text, "Alert didn't show up"

    class TestFrames:
        def test_frames(self,driver):
            frames_page = FramesPage(driver, "https://demoqa.com/frames")
            frames_page.open()
            result_frame1 = frames_page.check_frame()
            result_frame2 = frames_page.check_frame('frame2')
            assert result_frame1 == ['This is a sample page', '500px', '350px'], "The frame1 doesn't exists"
            assert result_frame2 == ['This is a sample page', '100px', '100px'], "The frame2 doesn't exists"

    class TestNestedFrames:
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frame_page.open()
            child_text, parent_text = nested_frame_page.check_nested_frames()
            assert child_text == 'Child Iframe', "The child frame doesn't exists"
            assert parent_text == 'Parent frame', "The parent frame doesn't exists"

    class TestModalDialogs:
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = TestModalPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()

            assert small[1] < large[1], 'text from large dialog is less than text from small dialog'
            assert small[0] == 'Small Modal', 'the header is not "Small Modal"'
            assert large[0] == 'Large Modal', 'the header is not "Large Modal"'



