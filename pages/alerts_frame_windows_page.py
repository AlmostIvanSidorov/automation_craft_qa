import random
import time
from locators.alerts_frame_windows_locators import *
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = BrowserWindowPageLocators()

    def checked_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title
    
    def checked_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW).text
        return text_title
    
class AlertsPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = AlertsLocators()

    
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text
    
    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_AFTER_5_SEC_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text
    
    def check_alert_confirm_box(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_BOX_ALERT_RESULT).text
        return text_result
    
    def check_prompt_alert(self):
        text = f"auto_test{random.randint(0, 99)}"
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMPT_RESULT).text
        return text, text_result
    
class FramesPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = FramesLocators()

    def check_frame(self, frame_number = None):
        if frame_number is None:
            print('Default frame was taken')
            frame_number = 'frame1'

        if frame_number == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()

            return [text, width, height]
        
        if frame_number == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()

            return [text, width, height]

