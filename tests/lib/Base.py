"""
Base class definitions to be used in place of when unittest.TestCase is applicable
    Purpose is to support different types of webdriver instances 
    Inherit from desired base class when certain webdriver settings are desired
"""
import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


# define globals
__app_root__ = os.path.abspath(os.path.dirname(__file__))

# define driver paths relative to app root
__driver_exe_dir__ = os.path.join(__app_root__, '../..', 'drivers')
__chrome_path__ = os.path.join(__driver_exe_dir__, 'chromedriver.exe')

class ChromeTest(unittest.TestCase):
    """for running chrome browser tests on localhost"""
    @classmethod
    def setUpClass(cls):
        print('ChromeTest.setUpClass')
        cls.driver = webdriver.Chrome(__chrome_path__) # open browsers
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5) # seconds

    @classmethod
    def tearDownClass(cls):
        """teardown environment after all test functions are executed in test class"""
        print('ChromeTest.tearDownClass')
        time.sleep(3)
        cls.driver.quit() # close browsers
    
    # cls.driver.quit() # close browsers
    
