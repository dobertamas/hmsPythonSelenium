import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import LoginPageLocators, MainPageLocators
from hms.utilities.custom_logger import custom_logger
from hms.utilities.filereader import FileReader


class LoginPage(BasePage):
    """
    Page Object Model for the HMS Admin login page.
    Methods:
        start: to visit the page this class is modeling, using the inherited (fom BasePage) open method
        login: to perform the actual login. Returns True or False
        enter_username
        enterPassword
        clickLoginButton
        verify_that_logged_in: using xpath locators ut verifies that we are actually on the expected page
    """
    log = custom_logger(logging.DEBUG)

    def start(self):
        """
        The start method also verifies the page title after getting the url.
        """
        self.url = '/config/list'
        self.open(self.url)
        self.log.info("Starting the login page ")
        self.assertIn("HMS", self._driver.title)

    def login(self):
        file_reader = FileReader()
        username = file_reader.get_username()
        self.enter_username(username.strip("\n"))
        file_reader = FileReader()
        password = file_reader.get_password()
        self.enterPassword(password.strip("\n"))
        self.clickLoginButton()
        if 'HMS' in self._driver.title:
            self.log.debug("Successful login ")
            return True
        else:
            self.log.debug("Login failed ")
            return False

    def enter_username(self, username):
        self.sendKeys(username, LoginPageLocators.USERNAME_FIELD, "name")

    def enterPassword(self, password):
        self.sendKeys(password, LoginPageLocators.PASSWORD_FIELD, "name")

    def clickLoginButton(self):
        self.elementClick(LoginPageLocators.LOGIN_BUTTON, "name")

    def verify_that_logged_in(self):
        self.assertTrue(self.isElementPresent(MainPageLocators.ACTIVE_CLASS, "xpath"),
                        "We are not on the expected page")
        self.assertTrue(self.isElementPresent(MainPageLocators.ACTIVE_CLASS_CONTAINS, "xpath"),
                        "We are not on the expected page")
