from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def input_text_box(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((MainPageLocators.TEXT_BOX))
        )
        element = self.driver.find_element(*MainPageLocators.TEXT_BOX)
        element.send_keys("Unit test" + Keys.ENTER)
        
    def click_go_button(self):
        WebDriverWait(self.driver, 5).until( # type: ignore
            EC.presence_of_element_located((MainPageLocators.GO_BUTTON))
        )
        element2 = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element2.click()

class SearchReseultsPage(BasePage):
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
