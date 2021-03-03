"""
Locators are an ordered value pair (tuple) consisting of a "By" method and an associated string
    Purpose is to add an level of indirection to decouple a web element's "address" from business logic
    enacting on the element.   
"""
from selenium.webdriver.common.by import By

# Example page locator definition

#     class MainPageLocators(object):
#         SOME_TEXTBOX = (By.NAME, 'username')
#         SOME_OTHER_TEXTBOX = (By.NAME, 'password')
#         OK_BUTTON = (By.CSS_SELECTOR, 'input[ng-click="ok()"]')
#         CANCEL_BUTTON = (By.CLASS_NAME, 'close')
#         TABLE_ITEMS = (By.ID, 'mymodal')
#         TABLE_LABEL = (By.XPATH, '//*[@id="123"]')

class WeightWatchLocators():
    #New locators for WW
    ASSERT_TITLE = (By.XPATH, '//h1[contains(text(), "WW (Weight Watchers): Weight Loss Program & Wellness Help | WW USA")]')
    VIRTUAL_WORKSHOP = (By.CSS_SELECTOR, 'a[class="Button_button__RwVHT MenuItem_menu-item__link__2qTtx SecondaryMenu_subMenuItem__1aNOr Button_button--no-style__3CpTl"]')
    ATTEND_DROPDOWN = (By.XPATH, '//span[contains(text(), "Attend")]')
    FIND_WW_STUDIOS_TITLE = (By.XPATH, '//title[contains(text(), "Find WW")]') 
    FIND_WW_STUDIOS_TITLE = (By.XPATH, '//title[contains(text(), " Studios & Meetings Near You | WW USA ")]')
    
    #SECOND_TITLE = (By.XPATH, '//meta[@property="og:title")]').__getattribute__("content")

    FIND_WORKSHOPTITLE = (By.XPATH, '//h1[contains(text(), "Find Your Workshop")]')
    STUDIO = (By.XPATH, '//span[contains(text(), "Studio")]')
    SEARCH_WORKSHOP = (By.ID, 'location-search')
    SEARCH_ENTER = (By.ID, 'location-search-cta')
    FIRST_SEARCH = (By.CSS_SELECTOR, 'a[class="linkUnderline-1_h4g"]')
    FIRST_SEARCH_TITLE = (By.XPATH, '//a[contains(text(), "WW Studio Flatiron")]')
    DISTANCE = (By.XPATH, '//span[contains(text(),"0.49 mi")]')
    BUSINESS_HOURS = (By.XPATH, '//span[@class="time-35INk"]')
    BUSINESS_HOUR_DROPDOWN = (By.XPATH, '//div[@class="title-3o8Pv"]')
    #SUNDAY = (By.XPATH, '//span[contains(text(),"SUN")]')
    USER_JOHN = (By.XPATH, '//span[contains(text(),"JOHN B.")]')
    USER_JOSHUA = (By.XPATH, '//span[contains(text(),"JOSHUA S.")]')
    SUN = (By.XPATH,'//span[contains(text(),"SUN")]')
    MON = (By.XPATH,'//span[contains(text(),"MON")]')
    TUE = (By.XPATH,'//span[contains(text(),"TUE")]')
    WED = (By.XPATH,'//span[contains(text(),"WED")]')
    THU = (By.XPATH,'//span[contains(text(),"THU")]')
    FRI = (By.XPATH,'//span[contains(text(),"FRI")]')
    SAT = (By.XPATH,'//span[contains(text(),"SAT")]')

class CommonLocators():
    #Organization / Location options under dropdown
    ASSERT_TITLE = (By.XPATH, '//h1[contains(text(), "WW (Weight Watchers): Weight Loss Program & Wellness Help | WW USA")]')
    

    
