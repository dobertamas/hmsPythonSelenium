import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import LocalRecTeamMemberAdminPageLocators
from hms.utilities.custom_logger import custom_logger


class LocalRecTeamMemberAdminPage(BasePage):
    log = custom_logger(logging.DEBUG)

    def start(self):
        self.url = '/localRecTeamMember/userList'
        self.open(self.url)
        self.log.info("Starting the LocalRec TeamMember Admin page ")
        self.assertIn("Local Recommendations Team Member Admin", self._driver.title)

    def verify_table_first_column(self):
        self.isElementPresent(LocalRecTeamMemberAdminPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")

        element = self.getElement(LocalRecTeamMemberAdminPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")
        self.assertEqual('FSQ User ID', element.text)
        return element.text
