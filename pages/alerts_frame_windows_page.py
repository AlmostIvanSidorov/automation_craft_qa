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
        
class NestedFramesPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = NestedFramesLocators()

    def __check_frame_text(self, frame_locator, text_locator):
        frame = self.element_is_present(frame_locator)
        self.driver.switch_to.frame(frame)
        text = self.element_is_present(text_locator).text
        return text

    def check_nested_frames(self):
        parent_text = self.__check_frame_text(self.locators.PARENT_FRAME, self.locators.PARENT_TEXT)
        child_text = self.__check_frame_text(self.locators.CHILD_FRAME, self.locators.CHILD_TEXT) # parent_text switch us to parent frame so we can switch to child frame

        return child_text, parent_text
    
class TestModalPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = TestModalLocators()

    def __check_modal_dialog(self,window_button, title_content, body_content, close_button):
        self.element_is_visible(window_button).click()
        title = self.element_is_visible(title_content).text
        body = self.element_is_visible(body_content).text
        self.element_is_visible(close_button).click()

        return title, body

    def check_modal_dialogs(self):
        title_small, body_small_text = self.__check_modal_dialog(self.locators.SMALL_MODAL_BUTTON,
                                                                  self.locators.TITLE_SMALL_MODAL,
                                                                  self.locators.BODY_SMALL_MODAL,
                                                                  self.locators.CLOSE_SMALL_MODAL_BUTTON)
        
        title_large, body_large_text = self.__check_modal_dialog(self.locators.LARGE_MODAL_BUTTON,
                                                            self.locators.TITLE_LARGE_MODAL,
                                                            self.locators.BODY_LARGE_MODAL,
                                                            self.locators.CLOSE_LARGE_MODAL_BUTTON)
        
        
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]


