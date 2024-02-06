from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button#tabButton")
    TITLE_NEW = (By.CSS_SELECTOR, 'h1#sampleHeading')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button#windowButton')

class AlertsLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#alertButton')
    APPEAR_ALERT_AFTER_5_SEC_BUTTON = (By.CSS_SELECTOR, 'button#timerAlertButton')
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#confirmButton')
    PROMPT_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, 'button#promtButton')

    CONFIRM_BOX_ALERT_RESULT = (By.CSS_SELECTOR, 'span#confirmResult')
    PROMPT_RESULT = (By.CSS_SELECTOR, 'span#promptResult')

class FramesLocators:
    FIRST_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')

    SECOND_FRAME = (By.CSS_SELECTOR, 'iframe#frame2')

    TITLE_FRAME = (By.CSS_SELECTOR, 'h1#sampleHeading')

class NestedFramesLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe#frame1')
    PARENT_TEXT = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_TEXT = (By.CSS_SELECTOR, 'body p')

class TestModalLocators:

    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#showSmallModal')
    CLOSE_SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#closeSmallModal')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div.modal-body')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-sm')

    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#showLargeModal')
    CLOSE_LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button#closeLargeModal')
    BODY_LARGE_MODAL = (By.CSS_SELECTOR, 'div.modal-body')
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, 'div#example-modal-sizes-title-lg')


