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

class RadioButtonPageLocators:
    RADIO_BUTTONS = (By.CSS_SELECTOR, 'label.custom-control-label')
    SELECTED_BUTTON = (By.CSS_SELECTOR, 'span.text-success')

class WebTablePageLocators:
    #add person form
    ADD_BUTTON =  (By.CSS_SELECTOR, 'button#addNewRecordButton')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, 'input#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input#userEmail')
    AGE_INPUT = (By.CSS_SELECTOR, 'input#age')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input#salary')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input#department')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button#submit')

    #tables

    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")

    SEARCH_INPUT = (By.CSS_SELECTOR,"input#searchBox")
    DELETE_BUTTON = (By.CSS_SELECTOR,"span[title='Delete']")
    RAW_PARENT = ".//ancestor::div[@class='rt-tr-group']"

