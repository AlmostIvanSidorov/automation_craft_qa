from selenium.webdriver.common.by import By

class AccordianLocators:
    SECTION_FIRST = (By.CSS_SELECTOR, 'div#section1Heading')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div#section1Content p')
    SECTION_SECOND = (By.CSS_SELECTOR, 'div#section2Heading')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div#section2Content p')
    SECTION_THIRD = (By.CSS_SELECTOR, 'div#section3Heading')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div#section3Content p')

class AutoCompleteLocators:

    MULTI_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteMultipleInput')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div.css-1rhbuit-multiValue')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div.auto-complete__indicator svg path')

    SINGLE_VALUE = (By.CSS_SELECTOR, 'div.auto-complete__single-value.css-1uccc91-singleValue')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input#autoCompleteSingleInput')

class DatePickerLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input#datePickerMonthYearInput')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select.react-datepicker__month-select')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select.react-datepicker__year-select')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')

    DATE_TIME_INPUT = (By.CSS_SELECTOR, 'input#dateAndTimePickerInput')
    DATE_TIME_SELECT_MONTH = (By.CSS_SELECTOR, 'div.react-datepicker__month-read-view')
    DATE_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__month-option')
    DATE_TIME_SELECT_YEAR = (By.CSS_SELECTOR, 'div.react-datepicker__year-read-view')
    DATE_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__year-option')
    DATE_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li.react-datepicker__time-list-item')


