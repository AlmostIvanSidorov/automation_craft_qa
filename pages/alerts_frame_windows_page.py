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
