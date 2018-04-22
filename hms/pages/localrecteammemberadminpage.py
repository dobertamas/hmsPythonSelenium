import logging

from hms.pages.basepage import BasePage
from hms.utilities.custom_logger import custom_logger


class LocalRecTeamMemberAdminPage(BasePage):
    pass

    log = custom_logger(logging.DEBUG)

    def start(self):
        self.url = '/localRecTeamMember/userList'
        self.open(self.url)
        self.log.info("Starting the LocalRec TeamMember Admin page ")
        self.assertIn("Local Recommendations Team Member Admin", self._driver.title)
