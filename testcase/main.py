import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page
import time

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.service = Service(excutable_path="chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.get("https://www.python.org/")

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        mainPage.input_text_box()
        mainPage.click_go_button()
        search_results_page = page.SearchReseultsPage(self.driver)
        assert search_results_page.is_results_found()
        
    def tearDown(self):
        time.sleep(10)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()