from selenium.webdriver.common.keys import Keys
from locators.locators import WeightWatchLocators
from locators.locators import CommonLocators
from pom.BasePage import BasePage
import time
### Beginning for Wait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
### End for Wait

class WeightWatchersPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.route = '#/login?returnUrl=%2Foverview' 
    
    def get_page_title(self):
        page_title = self.driver.find_element(*CommonLocators.ASSERT_TITLE)
        return page_title.text
    
    def get_studios_title(self):
        page_title = self.driver.find_element(*WeightWatchLocators.FIND_WW_STUDIOS_TITLE)
        return page_title.text
    

    def click_attend(self):
        click_attend = self.driver.find_element(*WeightWatchLocators.ATTEND_DROPDOWN)
        click_attend.click()
        time.sleep(2)

    def click_virtual_workshop_button(self):
        click_virtual_workshop_button = self.driver.find_element(*WeightWatchLocators.VIRTUAL_WORKSHOP)
        click_virtual_workshop_button.click()
        time.sleep(2)

    def studio_click(self):
        click_studio = self.driver.find_element(*WeightWatchLocators.STUDIO)
        click_studio.click()
        time.sleep(2)
    
    def workshop_title(self):
        workshop_title = self.driver.find_element(*WeightWatchLocators.FIND_WORKSHOPTITLE)
        return workshop_title.text
    
    def enter_location(self, studio_location):
        enter_location = self.driver.find_element(*WeightWatchLocators.SEARCH_WORKSHOP)
        enter_location.clear()
        enter_location.send_keys(studio_location)

    def click_search(self):
        click_studio = self.driver.find_element(*WeightWatchLocators.SEARCH_ENTER)
        click_studio.click()
        time.sleep(2)

    def click_firstsearch(self):
        click_firstsearch = self.driver.find_element(*WeightWatchLocators.FIRST_SEARCH)
        click_firstsearch.click()
        time.sleep(2)

    def firstsearch_title(self):
        #waiting_for_element = self.wait_element_is_visible(LoginPageLocators.FIRST_SEARCH_TITLE, self.timeout_time_default)
        workshop_title = self.driver.find_element(*WeightWatchLocators.FIRST_SEARCH_TITLE)
        return workshop_title.text

    def distance(self):
        #waiting_for_element = self.wait_element_is_visible(LoginPageLocators.DISTANCE, self.timeout_time_default)
        distance = self.driver.find_element(*WeightWatchLocators.DISTANCE)
        return distance.text
    
    def click_businesshours(self):
        click_businesshours = self.driver.find_element(*WeightWatchLocators.BUSINESS_HOUR_DROPDOWN)
        click_businesshours.click()
        time.sleep(2)
    
    def today_hour(self):
        today_hour = self.driver.find_element(*WeightWatchLocators.BUSINESS_HOUR)
        return today_hour.text
    
    def today_hours(self):
        #waiting_for_element = self.wait_element_is_visible(LoginPageLocators.BUSINESS_HOURS, self.timeout_time_default)
        hours_working = self.driver.find_element(*WeightWatchLocators.BUSINESS_HOURS)
        return hours_working.text

    def days(self):
        sunday = self.driver.find_element(*WeightWatchLocators.SUN)
        return sunday.text

    def user_A(self,print_meetings):
        #count = 0
        user_A = self.driver.find_element(*WeightWatchLocators.USER_JOHN)
        user_B = self.driver.find_element(*WeightWatchLocators.USER_JOSHUA)
        users = [user_A, user_B]
        #text = "JOHN B.", "JOHN B.", "JOHN.B"
        #counter1 = text.count(user_A)
        #if(text == user_A):
        #    count = count+1
        #print("Meetings".format(user_A(users,print_meetings)))
        return print_meetings.count(users)
    
    def print_meetings(self):
        Sunday = self.driver.find_element(*WeightWatchLocators.SUN)
        return Sunday.text
        #Thursday = self.driver.find_element(*WeightWatchLocators.THU)
       
    