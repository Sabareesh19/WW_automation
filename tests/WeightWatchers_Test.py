import unittest
import HtmlTestRunner
import time

from selenium.webdriver.common.keys import Keys
from lib.Base import ChromeTest # TestCase base class to inherit from
from lib.utils import TestSuiteExtensions # support methods for generating test suites
from pom.WeightWatchersPage import WeightWatchersPage

### Beginning import for Wait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
### End import for Wait
 
class WeightWatchersClass(ChromeTest):
	
	#@unittest.skip("Skip")
	def test_01_loaded_pagetitle(self):
		"""check page title of Weight Watchers"""
		print('running test_01')
		expected_page_title = 'WW (Weight Watchers): Weight Loss Program & Wellness Help | WW USA'
		weight_watchers_page = WeightWatchersPage(self.driver)
		weight_watchers_page.load_page()
		actual_page_title = weight_watchers_page.get_page_title()
		self.assertEqual(expected_page_title, actual_page_title)
		weight_watchers_page.click_attend()
		time.sleep(3)
		weight_watchers_page.click_virtual_workshop_button()
		time.sleep(3)

	@unittest.skip("Skip")
	def test_02_studios_pagetitle(self):
		"""check page title of Find WW Studios"""
		print('running test_02')
		expected_page_title1 = 'Find WW Studios & Meetings Near You | WW USA'
		expected_page_title = 'Studios & Meetings Near You | WW USA '
		weight_watchers_page = WeightWatchersPage(self.driver)
		actual_page_title = weight_watchers_page.get_studios_title()
		print("|| The current page title is")
		print(actual_page_title)
		print("||")
		self.assertEqual(expected_page_title, actual_page_title)
		
	
	#@unittest.skip("Skip")
	def test_03_find_a_workshop(self):
		"""Find a workshop"""
		print('running test_03')
		studio_location = '10011'
		expected_page_title = 'Find Your Workshop'
		weight_watchers_page = WeightWatchersPage(self.driver)
		actual_page_title = weight_watchers_page.workshop_title()
		self.assertEqual(expected_page_title, actual_page_title)
		weight_watchers_page.studio_click()
		time.sleep(3)
		weight_watchers_page.enter_location(studio_location)
		time.sleep(3)
		weight_watchers_page.click_search()
		time.sleep(3)

	#@unittest.skip("Skip")
	def test_04_print_search_result(self):
		"""Print the first search result"""	
		print('running test_04')
		expected_page_title = 'WW Studio Flatiron'
		weight_watchers_page = WeightWatchersPage(self.driver)
		#print(distance, studio_name)
		actual_page_title = weight_watchers_page.firstsearch_title()
		print("|| The name/title of first result is ")
		print(actual_page_title)
		print("||")
		actual_distance = weight_watchers_page.distance()
		print("|| The distance of studio is ")
		print(actual_distance)
		print("||")
		weight_watchers_page.click_firstsearch()
		self.assertEqual(expected_page_title, actual_page_title)
		time.sleep(3)


	#@unittest.skip("Skip")
	def test_05_display_business_hours(self):
		"""Display today's business hours"""
		print('running test_05')
		weight_watchers_page = WeightWatchersPage(self.driver)
		weight_watchers_page.click_businesshours()
		working_hour = weight_watchers_page.today_hour()
		print("|| Currently, the studio is expected to be ")
		print(working_hour)
		print("||")
		working_hours = weight_watchers_page.today_hours()
		print(" The next scheduled hours of operation is between ")
		print(working_hours)
		print("||")
		#self.assertEqual(expected_login_error, actual_login_error)

	
	#@unittest.skip("Skip")
	#Enter username and password more than maximum characters/digits and login
	def test_06_username_password_morethanmax_characters(self):
		"""check username and password more than maximum characters"""
		print('running test_06')
		Expected_title = "SUN"
		weight_watchers_page = WeightWatchersPage(self.driver)
		actual_title = weight_watchers_page.days()
		self.assertEqual(Expected_title,actual_title)
		time.sleep(3)	
	

if __name__ == '__main__':
    ### generate test suite ###
    test_suite = TestSuiteExtensions.suite_from_testclass(WeightWatchersClass)

    ### setup test runner ###
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    # runner = unittest.TextTestRunner(verbosity=2)

    ### run test suite ###
    runner.run(test_suite)

#@unittest.skip("Skip")
	#def test_05_print_number_of_meeting_eachperson(self):
	#	"""Meeting each person """
	#	print('running test_05')
	#	count1 = 0
	#	weight_watchers_page = WeightWatchersPage(self.driver)
	#	user_a1 = weight_watchers_page.user_A()
	#	text="JOHN B."
	#	for i in user_a1:
	#		if i in user_a1:
	#			count1 = count1+ 1
	#	print(" || The meeting is")
	#	print(user_a1)
	#	print(count1)
	#	print("||")

	#@unittest.skip("Skip")
	#Enter valid username and password and login
	#def test_07_valid_username_and_password(self):
	#	"""check valid username and password """
	#	print('running test_07')
	#	Sunday = "SUN"
		#user_A = 'JOHN B.'
	#	weight_watchers_page = WeightWatchersPage(self.driver)
	#	print("The meetings are", weight_watchers_page.user_A(Sunday))
	#	time.sleep(3)

		#weight_watchers_page.load_page()