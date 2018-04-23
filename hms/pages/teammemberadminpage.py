import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import LocalRecTeamMemberAdminPageLocators
from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class LocalRecTeamMemberAdminPage(BasePage):
    log = custom_logger(logging.DEBUG)

    def start(self):
        """
        The start method also verifies the page title after getting the url.
        """
        self.url = '/localRecTeamMember/userList'
        self.open(self.url)
        self.log.info("Starting the LocalRec TeamMember Admin page ")
        self.assertIn("Local Recommendations Team Member Admin", self._driver.title)

    def verify_table_first_column(self):
        self.isElementPresent(LocalRecTeamMemberAdminPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")

        element = self.getElement(LocalRecTeamMemberAdminPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")
        self.assertEqual(config.LOCAL_TDOBER['TEAM_MEMBER_ADMIN_FIRST_COLUMN_TEXT'].strip("\n"), element.text)
        return element.text
