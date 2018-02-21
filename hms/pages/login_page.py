import logging

from hms.pages.base_page import Base_Page
from hms.pages.locators import Locators
from hms.utilities.custom_logger import customLogger


class Login_Page(Base_Page):
    log = customLogger(logging.DEBUG)

    def start(self):
        self.url = '/config/list'
        self.open(self.url)
        self.log.info(" starting the login page ")
        self.assertIn("HMS", self.driver.title)

    def login(self, username="admin", password="admin"):

        self.enter_username(username)
        self.enterPassword(password)
        # time.sleep(30)
        self.clickLoginButton()
        if 'HMS: Global Prefs' in self.driver.title:
            self.log.info(" successful login ")
            return True
        else:
            self.log.info(" login failed ")
            return False

    def enter_username(self, username):
        self.sendKeys(username, Locators._username_field, "name")

    def enterPassword(self, password):
        self.sendKeys(password, Locators._password_field, "name")

    def clickLoginButton(self):
        self.elementClick(Locators._login_button, "name")
