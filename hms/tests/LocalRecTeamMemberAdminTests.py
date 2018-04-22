import logging
import time
import unittest

from hms.pages.driverfactory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities.custom_logger import custom_logger


class LocalRecTeamMemberAdminTests(unittest.TestCase):
    log = custom_logger(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        driver_object = DriverFactory()
        cls.driver = driver_object.get_web_driver("firefox")
        login_page = PageFactory.get_page_object("login", cls.driver)
        login_page.login()
        time.sleep(3)

    def test_happy_path_visit_teamMember_admin_page(self):
        team_member_admin_page = PageFactory.get_page_object("teammemberadmin", self.driver)
        team_member_admin_page.start()
