import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import FindMemberPageLocators
from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class FindMemberPage(BasePage):
    """
        Page Object Model for the HMS Find Member page.
        Methods:
            start: to visit the page this class is modeling, using the inherited (fom BasePage) open method
        """
    log = custom_logger(logging.DEBUG)

    def start(self):
        """
        The start method also verifies the page title after getting the url.
        """
        self.url = '/member/find'
        self.open(self.url)
        self.log.info("Starting the find member page ")
        self.assertIn("HMS: Find Member", self._driver.title)

    def fetch_member(self):
        self.enter_member_id(config.LOCAL_TDOBER['FETCH_MEMBER_TEST_ID'].strip("\n"))
        self.click_fetch_button()

    def enter_member_id(self, member_id):
        self.sendKeys(member_id, FindMemberPageLocators.MEMBER_ID_FIELD, "id")

    def click_fetch_button(self):
        self.elementClick(FindMemberPageLocators.FETCH_BUTTON, "xpath")
