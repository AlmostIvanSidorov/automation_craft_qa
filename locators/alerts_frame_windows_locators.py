from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    TITLE_NEW = (By.CSS_SELECTOR, 'h1#sampleHeading')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')

class AlertsLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#alertButton')
    APPEAR_ALTER_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button#timerAlertButton')
    CONFIRM_BOX_ALLERT_BUTTON = (By.CSS_SELECTOR, 'button#confirmButton')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#promtButton')
