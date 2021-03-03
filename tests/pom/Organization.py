from selenium.webdriver.common.keys import Keys
from locators.locators import LoginPageLocators
from locators.locators import CommonLocators
from locators.locators import OrganizationLocators
from pom.BasePage import BasePage
from selenium.common.exceptions import NoSuchElementException
import time
import re


class Organization(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.route = '#/users'

    # type_password = BasePage.type_factory(LoginPageLocators.PASSWORD_TEXTBOX)
    # click_login = BasePage.click_factory(LoginPageLocators.LOGIN_BUTTON)
    # click_password_textbox = BasePage.click_factory(LoginPageLocators.PASSWORD_TEXTBOX)  

    # Add user icon
    #click_add_user_icon = BasePage.click_factory(UserManagementLocators.ADD_ICON)
    #click_add_multiple_user_icon = BasePage.click_factory(UserManagementLocators.ADD_MULTIPLE_ICON)
    #click_edit_user_icon = BasePage.click_factory(UserManagementLocators.EDIT_ICON)
    #click_delete_user_icon = BasePage.click_factory(UserManagementLocators.DELETE_ICON)
    #click_reset_password_icon = BasePage.click_factory(UserManagementLocators.RESET_PASSWORD_ICON)
    #click_refresh_icon = BasePage.click_factory(UserManagementLocators.REFRESH_ICON)

    # def click_edit_user_icon(self):
    #     user_management_edit_user = self.driver.find_element(*UserManagementLocators.EDIT_ICON)
    #     user_management_edit_user.click()
    #     time.sleep(1)
    
    #Delete user icon
    # def click_delete_user_icon(self):
    #     delete_user_icon = self.driver.find_element(*UserManagementLocators.DELETE_ICON)
    #     delete_user_icon.click()
    #     time.sleep(2)
    
    #Reset Password icon
    # def click_reset_password_icon(self):
    #     reset_password_icon = self.driver.find_element(*UserManagementLocators.RESET_PASSWORD_ICON)
    #     reset_password_icon.click()
    #     #time.sleep(1)

    def enter_organization_name(self,orgname):
        enter_first_name = self.driver.find_element(*OrganizationLocators.ORGANIZATION_NAME_INPUT)
        enter_first_name.clear()
        enter_first_name.send_keys(orgname)

    def enter_organizationdisplay_name(self,orgdisplayname):
        enter_first_name = self.driver.find_element(*OrganizationLocators.ORGANIZATION_DISPLAY_NAME_INPUT)
        enter_first_name.clear()
        enter_first_name.send_keys(orgdisplayname)
    
    def enter_contract_email(self,contractemail):
        enter_first_name = self.driver.find_element(*OrganizationLocators.CONTRACT_EMAIL_INPUT)
        enter_first_name.clear()
        enter_first_name.send_keys(contractemail)
    
    def contains_email(self,containsemail):
        enter_first_name = self.driver.find_element(*OrganizationLocators.CONTAINS_EMAIL)
        enter_first_name.clear()
        enter_first_name.send_keys(containsemail)