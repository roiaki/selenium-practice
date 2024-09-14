from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains 

from selenium.webdriver.common.keys import Keys
import time

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def click_account_options(self):
        # wait for first element presence
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((MainPageLocators.ACCOUNT_OPTIONS))
        )

        # account options
        element = self.driver.find_element(*MainPageLocators.ACCOUNT_OPTIONS)
        element.click()

        # wait for first element presence
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((MainPageLocators.REGISTER))
        )

        # register
        # ActionChains複数のマウスやキーボードの操作を連続的に実行するためのもの
        element = self.driver.find_element(*MainPageLocators.REGISTER)
        action = ActionChains(self.driver)
        time.sleep(2)
        action.move_to_element(element).perform()
        time.sleep(2)
        element.click()

class  RegisterPage(BasePage):
    def input_account_information(self):
        # wait for first element presence
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((RegisterPageLocators.FIRST_NAME))
        )

        # first name
        element = self.driver.find_element(*RegisterPageLocators.FIRST_NAME)
        element.click()
        time.sleep(1)
        element.send_keys('test_first_name')
        time.sleep(1)

        # last name
        element = self.driver.find_element(*RegisterPageLocators.LAST_NAME)
        element.click()
        time.sleep(1)
        element.send_keys('test_last_name')
        time.sleep(1)

        # email
        element = self.driver.find_element(*RegisterPageLocators.EMAIL)
        element.click()
        time.sleep(1)
        element.send_keys('test@unittest202409141000.com')
        time.sleep(1)

        # telephone
        element = self.driver.find_element(*RegisterPageLocators.TELEPHONE)
        element.click()
        time.sleep(1)
        element.send_keys('012345678901234567890123456789012')
        time.sleep(1)

        # password
        element = self.driver.find_element(*RegisterPageLocators.PASSWORD)
        element.click()
        time.sleep(1)
        element.send_keys('P@ssw0rd')
        time.sleep(1)

        # password confirm
        element = self.driver.find_element(*RegisterPageLocators.PASSWORD_CONFIRM)
        element.click()
        time.sleep(1)
        element.send_keys('P@ssw0rd')
        time.sleep(1)

        # newsletter
        element = self.driver.find_element(*RegisterPageLocators.NEWSLETTER)
        element.click()
        time.sleep(1)

        # privacy policy
        element = self.driver.find_element(*RegisterPageLocators.PRIVACY_POLICY)
        element.click()
        time.sleep(1)

        # click on the continue button
        element = self.driver.find_element(*RegisterPageLocators.CONTINUE_BUTTON)
        element.click()
        time.sleep(2)

    def is_input_error(self):
        return "Telephone must be between 3 and 32 characters!" in self.driver.page_source
        time.sleep(2)

    def reinput_account_information(self):
        # telephone
        element = self.driver.find_element(*RegisterPageLocators.TELEPHONE)
        element.clear()
        time.sleep(1)
        element.send_keys('012345678')
        time.sleep(1)

        # click on the continue button
        element = self.driver.find_element(*RegisterPageLocators.CONTINUE_BUTTON)
        element.click()
        time.sleep(2)

class RegisterResultsPage(BasePage):
    def is_account_created(self):
        return "Your Account Has Been Created!" in self.driver.page_source
        time.sleep(2)