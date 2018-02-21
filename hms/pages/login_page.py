import logging

from hms.pages.base_page import Base_Page
from hms.pages.locators import Login_Page_Locators
from hms.utilities.custom_logger import customLogger
from hms.utilities.file_reader import File_Reader


class Login_Page(Base_Page):
    log = customLogger(logging.DEBUG)

    def start(self):
        self.url = '/config/list'
        self.open(self.url)
        self.log.info("Starting the login page ")
        self.assertIn("HMS", self.driver.title)

    def login(self, username="", password=""):
        file_reader = File_Reader()
        username = file_reader.get_username()
        self.enter_username(username)
        file_reader = File_Reader()
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
