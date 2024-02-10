from selenium.webdriver.common.by import By

class SortablePageLocators:
    
    TAB_LIST = (By.CSS_SELECTOR, "a#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "div.vertical-list-container div")

    GRID_LIST = (By.CSS_SELECTOR, "a#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "div.create-grid div")