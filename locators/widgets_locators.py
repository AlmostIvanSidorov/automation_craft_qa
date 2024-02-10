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

class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input.range-slider')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input#sliderValue')

class ProgressBarPageLocators:
    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button#startStopButton')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div.progress-bar') # aria-valuenow

class TabsPageLocators:

    TABS_WHAT = (By.CSS_SELECTOR, 'a#demo-tab-what')
    TABS_WHAT_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-what p')
    TABS_ORIGIN = (By.CSS_SELECTOR, 'a#demo-tab-origin')
    TABS_ORIGIN_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-origin p')
    TABS_USE = (By.CSS_SELECTOR, 'a#demo-tab-use')
    TABS_USE_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-use p')
    TABS_MORE = (By.CSS_SELECTOR, 'a#demo-tab-more') 
    TABS_MORE_CONTENT = (By.CSS_SELECTOR, 'div#demo-tabpane-more')

    tabs = {'What': 
        {'button': TABS_WHAT,
            'content': TABS_WHAT_CONTENT},
        'Origin': 
        {'button': TABS_ORIGIN,
            'content': TABS_ORIGIN_CONTENT},
        'Use': 
        {'button': TABS_USE,
            'content': TABS_USE_CONTENT},
        'More': 
        {'button': TABS_MORE,
            'content': TABS_MORE_CONTENT}}
    
class ToolTipsPageLocators:
    HOVER_BUTTON =(By.CSS_SELECTOR, 'button#toolTipButton')
    TOOL_TIP_HOVER_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    HOVER_FORM =(By.CSS_SELECTOR, 'input#toolTipTextField')
    TOOL_TIP_HOVER_FORM =(By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    CONTRARY_LINK =(By.XPATH, './/a[text()="Contrary"]')
    TOOL_TIP_CONTRARY_LINK =(By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    SECTION_LINK =(By.XPATH, './/a[text()="1.10.32"]')
    TOOL_TIP_SECTION_LINK =(By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div.tooltip-inner')






    


