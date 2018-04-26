import logging
import time
import unittest

from hms.pages.driver_factory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities.custom_logger import custom_logger


class LocalRecTeamMemberAdminTests(unittest.TestCase):
    log = custom_logger(logging.DEBUG)

    """
    Verifying LocalRec team admin page; the table elements and then the import and delete functions on the page.
    """

    @classmethod
    def setUpClass(cls):
        driver_object = DriverFactory()
        cls.driver = driver_object.get_web_driver("firefox")
        login_page = PageFactory.get_page_object("login", cls.driver)
        login_page.login()
        time.sleep(3)

    def test_happy_path_visit_teamMember_admin_page(self):
        """
        Visiting the page then verifying all table column texts
        """
        team_member_admin_page = PageFactory.get_page_object("teammemberadmin", self.driver)
        team_member_admin_page.verify_table_first_column()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
