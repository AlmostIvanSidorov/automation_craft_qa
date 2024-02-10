from selenium.webdriver.common.by import By

class SortablePageLocators:
    
    TAB_LIST = (By.CSS_SELECTOR, "a#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "div.vertical-list-container div")

    GRID_LIST = (By.CSS_SELECTOR, "a#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "div.create-grid div")

class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a#demo-tab-list")
    LIST_ITEM = (By.CSS_SELECTOR, "li.mt-2")
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, "li.mt-2.active")

    GRID_LIST = (By.CSS_SELECTOR, "a#demo-tab-grid")
    GRID_ITEM = (By.CSS_SELECTOR, "div.grid-container.mt-4 li")
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, "div.grid-container.mt-4 li.active")