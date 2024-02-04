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
            alert_page.check_see_alert()
            time.sleep(4)

