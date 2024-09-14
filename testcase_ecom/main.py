import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page
import time
import xmlrunner

class AccountRegistration(unittest.TestCase):
    
    def setUp(self):
        self.service = Service(excutable_path="chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get('https://tutorialsninja.com/demo')
        # self.driver.maximize_window

    def test_account_registration(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_account_options()

        RegisterPage = page.RegisterPage(self.driver)
        RegisterPage.input_account_information()
        assert RegisterPage.is_input_error()
        RegisterPage.reinput_account_information()

        register_results_page = page.RegisterResultsPage(self.driver)
        assert register_results_page.is_account_created()

    def tearDown(self):
        time.sleep(100)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner = xmlrunner.XMLTestRunner(output='test-reports'))