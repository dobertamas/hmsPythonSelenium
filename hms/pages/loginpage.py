import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import Login_Page_Locators, MainPageLocators
from hms.utilities.custom_logger import customLogger
from hms.utilities.filereader import FileReader


class LoginPage(BasePage):
    log = customLogger(logging.DEBUG)

    """
    To avoid the following when debugging through PyCharm:
    Unable to get repr for <class 'hms.pages.login_page.Login_Page'>
    """

    def __repr__(self):
        return "Login_Page"

    def start(self):
        self.url = '/config/list'
        self.open(self.url)
        self.log.info("Starting the login page ")
        self.assertIn("HMS", self.driver.title)

    def login(self, username="", password=""):
        file_reader = FileReader()
        username = file_reader.get_username()
        self.enter_username(username)
        file_reader = FileReader()
        password = file_reader.get_password()
        self.enterPassword(password)
        self.clickLoginButton()
        if 'HMS: Global Prefs' in self.driver.title:
            self.log.debug("Successful login ")
            return True
        else:
            self.log.debug("Login failed ")
            return False

    def enter_username(self, username):
        self.sendKeys(username, Login_Page_Locators.USERNAME_FIELD, "name")

    def enterPassword(self, password):
        self.sendKeys(password, Login_Page_Locators.PASSWORD_FIELD, "name")

    def clickLoginButton(self):
        self.elementClick(Login_Page_Locators.LOGIN_BUTTON, "name")

    def verify_that_logged_in(self):
        self.assertTrue(self.isElementPresent(MainPageLocators.ACTIVE_CLASS, "xpath"),
                        "We are not on the expected page")
        self.assertTrue(self.isElementPresent(MainPageLocators.ACTIVE_CLASS_CONTAINS, "xpath"))
