from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    FULL_NAME = (By.CSS_SELECTOR, "input#userName")
    EMAIL = (By.CSS_SELECTOR, "input#userEmail")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea#currentAddress")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea#permanentAddress")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")

class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span.rct-title")

    CHECKED_BOXES_LOCATOR = (By.CSS_SELECTOR, "svg.rct-icon.rct-icon-check")
    EXPECTED_RESULT_LOCATOR = (By.CSS_SELECTOR, "span.text-success")

    TITLE_ITEM = (".//ancestor::span[@class='rct-text']")


