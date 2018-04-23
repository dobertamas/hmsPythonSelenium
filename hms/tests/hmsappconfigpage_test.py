import logging
import time
import unittest

from hms.pages.driverfactory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities.custom_logger import custom_logger


class HmsAppConfigTests(unittest.TestCase):
    """
    Positive and negative tests for the HMS App Config page.
    """
    log = custom_logger(logging.DEBUG)

    @classmethod
    def setUpClass(cls):
        driver_object = DriverFactory()
        cls.driver = driver_object.get_web_driver("firefox")
        login_page = PageFactory.get_page_object("login", cls.driver)
        login_page.login()
        time.sleep(3)

    def test_happy_path_visit_hms_app_config_page(self):
        """
        Visiting the HMS App Config page; then verifying all table column texts
        """
        hms_app_config_page = PageFactory.get_page_object("hmsappconfig", self.driver)
        hms_app_config_page.verify_table_first_column()
        hms_app_config_page.verify_table_second_column()

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
