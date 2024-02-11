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

class ResizablePageLocators:
    
    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div#resizableBoxWithRestriction span.react-resizable-handle')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div#resizableBoxWithRestriction')


    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div#resizable span.react-resizable-handle')
    RESIZABLE = (By.CSS_SELECTOR, 'div#resizable')

class DroppablePageLocators:
    # Simple

    SIMPLE_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-simple')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div#draggable')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, 'div#simpleDropContainer div#droppable')

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-accept')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div#acceptable')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div#notAcceptable')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    # Prevent Propogation

    PREVENT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-preventPropogation')
    NOT_GREEDY_DROP_BOX_TEXT = (By.XPATH, './/div[@id="notGreedyDropBox"]/p[text()="Dropped!"]')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div#notGreedyInnerDropBox')
    GREEDY_DROP_BOX_TEXT = (By.XPATH, './/div[@id="greedyDropBox"]/p[text()="Outer droppable"]')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div#greedyDropBoxInner')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div#dragBox')

    # Revert Draggable

    REVERT_TAB = (By.CSS_SELECTOR, 'a#droppableExample-tab-revertable')
    WILL_REVERT = (By.CSS_SELECTOR, 'div#revertable')
    NOT_REVERT = (By.CSS_SELECTOR, 'div#notRevertable')
    DROP_HERE_REVERT = (By.CSS_SELECTOR, ' div#revertableDropContainer div#droppable')

class DraggablePageLocators:
    # Simple
    SIMPLE_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-simple')
    DRAG_ME = (By.XPATH, './/*[text()="Drag me"]')

    # Axis Restricted
    AXIS_TAB = (By.CSS_SELECTOR, 'a#draggableExample-tab-axisRestriction')
    ONLY_X = (By.CSS_SELECTOR, 'div#restrictedX')
    ONLY_Y = (By.CSS_SELECTOR, 'div#restrictedY')