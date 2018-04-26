import logging
import time
import unittest

from hms.pages.driver_factory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class FindMemberPageTests(unittest.TestCase):
    """
    Positive and negative tests for the HMS Find Member page.
    """
    log = custom_logger(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        driver_object = DriverFactory()
        cls.driver = driver_object.get_web_driver("firefox")
        login_page = PageFactory.get_page_object("login", cls.driver)
        login_page.login()
        time.sleep(3)

    def test_happy_path_visit_find_member_page(self):
        """
        Visiting the HMS Find Member page; then entering a valid member ID and clicking on Fetch button.
        """
        find_member_page = PageFactory.get_page_object("findmember", self.driver)
        find_member_page.fetch_member()
        time.sleep(3)
        member_detail_page = PageFactory.get_page_object_with_id_memberid("memberdetail", self.driver,
                                                                          config.LOCAL_TDOBER['FETCH_ID'].strip("\n"),
                                                                          config.LOCAL_TDOBER['FETCH_MEMBERID'].strip(
                                                                              "\n"))
        print(member_detail_page.verify_points())

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
