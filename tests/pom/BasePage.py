"""
This is a python implementation of the common "page object model" pattern
    This defines page objects which contain "test step" business logic to perform
    specific steps such as click, type, or more complex composite steps such as
    login, scroll, select radio/drop-down options.
    Aim to implement factory methods to avoid code duplication for common steps.

    Serves to decouple "test case" definition (TestClass file) 
    from test step business logic (Page object model-this module)

    Method names are in double underscore style with naming convention of "action_element"
    Why: the current style is to make it more intuitive for future implementations of keyword-driven testing
"""
from urllib.parse import urljoin
from selenium.webdriver.remote.webelement import WebElement
import time
from selenium.webdriver.support.ui import Select
import re
### Beginning for Wait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException
### End for Wait

class BasePage():
    """
    BasePage class to initialize the base page
    that will be called by all pages
    """
    def __init__(self, driver: WebElement):
        self.driver = driver
        self.default_wait = 3
        self.base_url = 'https://www.weightwatchers.com/us/' # weight watchers WW site
        self.route = ''
        self.timeout_time_default = 90

    def load_page(self):
        self.current_url = urljoin(self.base_url, self.route)
        self.driver.get(self.current_url)
        self.driver.implicitly_wait(10)

    @staticmethod
    def type_factory(locator):
        """factory method to generate type functions"""
        def type_func(self, value):
            """find element, clear field, type keys"""
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(value)
        return type_func

    @staticmethod
    def click_factory(locator):
        """factory method to generate click functions"""
        def click_func(self):
            """find element, click element, wait"""
            element = WebDriverWait(self.driver,self.timeout_time_default).until(ec.visibility_of_element_located((locator)))
            #element = self.driver.find_element(*locator)
            print("Click-Factory is now clicking: " + element.text + "||")
            try:
                element.click()
            except ElementClickInterceptedException:
                element = WebDriverWait(self.driver,self.timeout_time_default).until(ec.element_to_be_clickable((locator)))
                element.click()
            time.sleep(2)
        return click_func

    @staticmethod
    def select_factory(locator):
        """factory method to generate select functions"""
        def select_func(self, value):
            """find element, select option in the element, wait"""
            element = Select(self.driver.find_element(*locator))
            element.select_by_visible_text(value)
            time.sleep(2)
        return select_func

    @staticmethod
    def get_factory(locator):
        """factory method to generate get value functions"""
        def get_func(self, value):
            """find element, select option in the element, wait"""
            element = self.driver.find_element(*locator)
            value = element.text
            time.sleep(2)
            return value
        return get_func

    def wait_element_is_visible(self,locator,timeout_time):
        try:
            waiting_for_element = WebDriverWait(self.driver,timeout_time).until(ec.visibility_of_element_located((locator)))
            return waiting_for_element
        except TimeoutException:
            print("|| Unable to find element: ")
            print(locator)
    
    def wait_element_is_clickable(self,locator,timeout_time):
        try:
            waiting_for_element = WebDriverWait(self.driver,timeout_time).until(ec.element_to_be_clickable((locator)))
            return waiting_for_element
        except TimeoutException:
            print("|| Unable to click on element: ")
            print(locator)

    def wait_element_is_invisible(self,locator,timeout_time):
        try:
            waiting_for_element = WebDriverWait(self.driver,timeout_time).until(ec.invisibility_of_element((locator)))
            return waiting_for_element
        except TimeoutException:
            print("|| Could not wait for element to diappear: ")
            print(locator)
