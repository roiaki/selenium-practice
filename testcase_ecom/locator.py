from selenium.webdriver.common.by import By

class MainPageLocators(object):
    ACCOUNT_OPTIONS = (By.XPATH, '//a[@class="dropdown-toggle"]')
    REGISTER = (By.XPATH, '//a[text()="Register"]')

class RegisterPageLocators(object):
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    TELEPHONE = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    PASSWORD_CONFIRM = (By.ID, 'input-confirm')
    NEWSLETTER = (By.XPATH, '//input[@name="newsletter" and @value="1"]')
    PRIVACY_POLICY = (By.XPATH, '//input[@name="agree" and @value="1"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@value="Continue"]')

class RegisterResultsPageLocators(object):
    pass