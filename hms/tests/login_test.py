import logging
import time
import unittest

from hms.pages.driver_factory import DriverFactory
from hms.pages.pagefactory import PageFactory
from hms.utilities.custom_logger import custom_logger


class LoginTests(unittest.TestCase):
    log = custom_logger(logging.DEBUG)

    """
    Positive and negative tests for the login feature.
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
        self.assertTrue(login_page_object.login(), "Login failed")
        time.sleep(3)
        login_page_object.verify_that_logged_in()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
