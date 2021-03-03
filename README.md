# Quickstart for Simplified Testing Framework

This document is meant to be viewed with a Markdown previewer

## General Usage

### Environment requirements

1. IDE of your choice, VSCode is recommended.
2. Python packages used:

```shell
pip install selenium
pip install pylint
pip install html-testRunner
```

* virtualenv is recommended but not required.
* test runners are optional, import statements used in sample need to be commented out

### Call TestClass *.py file directly (useful for debugging)

Execute the below script
```shell
python pp_playtest_run.py
``` 
or

```shell
python YourTestClass*.py
```
Script into your IDEs launch/build/compile functions (e.g. F5 to run)

* Launch.json is provided for VSCode users

The HTML reports are generated after execution and available under WW_Project.

## My Architecture

Current architecture is:

* TestClass -> Page Object Model -> Locators

"TestClass" implements test cases by defining test steps:
An login example how the logic works is described here,

```python
class TestLoginClass(unittest.TestCase):
    def test_login_function(self):
        login_page.type_password()
        login_page.click_login()
```

"Page Object Model" implements business logic (methods) 
for conducting each individual test step action or a composite action

```python
class PageObjectClass():
    def click_login(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        element.click()
```

"Locators" defines ordered value-pairs which are essentially the "addresses" to web elements
    "web element" objects can be retrieved when locators as used in conjunction with
    webdriver's find_element/find_elements methods.

```python
class LoginPageLocators(object):
    """Locators for Login page"""
    USERNAME_TEXTBOX = (By.NAME, 'email')
    PASSWORD_TEXTBOX = (By.NAME, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'submit')
```
