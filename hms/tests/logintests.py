import logging
import time
import unittest

from hms.pages.driverfactory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities.custom_logger import custom_logger


class LoginTests(unittest.TestCase):
    log = custom_logger(logging.DEBUG)

    """
    The browser type is determined by supplying short name like 'chrome' or 'ff' or 'firefox'.
    The tests call the Driver_Factory class. Currently only local drivers are available.
    After obtaining a driver object we call the Page_Factory class, which returns a Login page object. 
    """

    @classmethod
    def setUpClass(cls):
        driver_object = DriverFactory()
        cls.driver = driver_object.get_web_driver("ff")
        # driver.maximize_window()

    def test_happy_path_login(self):
        """
        Positive test for the login feature. Providing valid username and password enables user to log in.
        """

        login_page_object = PageFactory.get_page_object("login", self.driver)

        is_successful = login_page_object.login()
        self.log.debug(" is_successful was: {} ".format(is_successful))
        self.assertTrue(is_successful, "Login failed")
        time.sleep(3)
        login_page_object.verify_that_logged_in()


if __name__ == '__main__':
    unittest.main()
