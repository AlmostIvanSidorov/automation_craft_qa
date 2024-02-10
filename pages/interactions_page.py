import random
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from generator.generator import generated_color, generated_date
from locators.interactions_locators import *
from selenium.common.exceptions import *
from pages.base_page import BasePage


class SortablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SortablePageLocators()
