import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import LoginPageLocators, MainPageLocators
from hms.utilities.custom_logger import custom_logger
from hms.utilities.filereader import FileReader


class LoginPage(BasePage):

    """
    Page Object Model for the HMS Admin login page.
    Attributes:

    """
    log = custom_logger(logging.DEBUG)

    def start(self):
        self.url = '/config/list'
        self.open(self.url)
        self.log.info("Starting the login page ")
        self.assertIn("HMS", self._driver.title)

    def login(self):
        file_reader = FileReader()
        username = file_reader.get_username()
        self.enter_username(username)
        file_reader = FileReader()
        password = file_reader.get_password()
        self.enterPassword(password)
        self.clickLoginButton()
        if 'HMS: Global Prefs' in self._driver.title:
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
        self.assertTrue(self.isElementPresent(MainPageLocators.ACTIVE_CLASS_CONTAINS, "xpath"))

    """
    To avoid the following when debugging through PyCharm:
    Unable to get repr for <class 'hms.pages.login_page.Login_Page'>
    """

    def __repr__(self):
        return "Login_Page"
