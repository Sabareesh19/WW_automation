import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

__app_root__ = os.path.abspath(os.path.dirname(__file__))

# define driver paths relative to app root
__driver_exe_dir__ = os.path.join(__app_root__, 'drivers')
__chrome_path__ = os.path.join(__driver_exe_dir__, 'chromedriver.exe')

driver = webdriver.Chrome(__chrome_path__)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.google.com")

class G_Locators():
    IM_FEELING_LUCKY_BUTTON = (By.ID, 'gbqfbb')
    SEARCH_TEXT_BOX = (By.NAME, 'q')
    SEARCH_TEXT_BOX_MICROPHONE = (By.CLASS_NAME, 'voice_search_button')
    ADVERTISING_LINK = (By.LINK_TEXT, 'Advertising')
    HOW_IT_WORKS_LINK = (By.PARTIAL_LINK_TEXT, 'How')
    GOOGLE_AD_HEADER = (By.TAG_NAME, 'h1')

    GOOGLE_SEARCH_BUTTON = (By.XPATH, '//input[@value="Google Search"])[2]')
    GOOGLE_CALENDAR_BUTTON = (By.XPATH, '//span [contains(text(), "Calendar")]')
    GOOGLE_APPS_BUTTON = (By.CSS_SELECTOR, 'a[title="Google apps"]')

class AddDevicesPageLocators():
    ADD_DEVICES_BUTTON = (By.CLASS_NAME, 'gtw-icon-devices-discover')
    ADD_DEVICES_NOW_OPTION = (By.LINK_TEXT, 'Add devices now')
    SAVED_DISCOVERY_SETTINGS_OPTION = (By.LINK_TEXT, 'Saved discovery settings')
    DISCOVERY_METHOD_DROPDOWN = (By.CLASS_NAME, 'c-btn')
    DISCOVERY_METHOD_BY_LOCAL_NETWORK_OPTION = (By.XPATH, '//label[contains(text(), "by local network")]')
    DISCOVERY_METHOD_BY_IP_ADDRESS_OR_HOST_NAME_OPTION = (By.XPATH, '//label[contains(text(), "By IP address or host name")]')
    DISCOVERY_METHOD_BY_IP_ADDRESS_RANGE_OPTION = (By.XPATH, '//label[contains(text(), "By IP address range")]')
    
    STARTING_IP_ADDRESS_FIELD = (By.XPATH, '//input[@class="form-control w-90 ng-pristine ng-invalid ng-touched"])[1]')
    ENDING_IP_ADDRESS_FIELD = (By.XPATH, '//input[@class="form-control w-90 ng-pristine ng-invalid ng-touched"])[2]')
    RESET_BUTTON= (By.XPATH, '//button[contains(text(), "Reset")]')
    RUN_BUTTON = (By.XPATH, '//button[contains(text(), "Run")]')
    CANCEL_BUTTON = (By.XPATH, '//button[contains(text(), "Cancel")]')


search_text_box = driver.find_element(*G_Locators.SEARCH_TEXT_BOX)
search_text_box.clear()
search_text_box.send_keys('Learn Selenium Locators')
time.sleep(3)

advertising_link = driver.find_element(*G_Locators.ADVERTISING_LINK)
advertising_link.click()
time.sleep(3)

# how_it_works_link = driver.find_element(*G_Locators.HOW_IT_WORKS_LINK)
# how_it_works_link.click()
# time.sleep(3)

google_ad_banner = driver.find_element(*G_Locators.GOOGLE_AD_HEADER)
print('\n', google_ad_banner.text)

driver.quit()