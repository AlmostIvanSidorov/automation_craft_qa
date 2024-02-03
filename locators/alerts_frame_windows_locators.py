from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    TITLE_NEW = (By.CSS_SELECTOR, 'h1#sampleHeading')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')
