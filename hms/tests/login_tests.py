import logging
import time
import unittest

from hms.pages.driver_factory import Driver_Factory
from hms.pages.page_factory import Page_Factory
from hms.utilities.custom_logger import customLogger


class Login_Tests(unittest.TestCase):
    """
    Tests positive and negative scenarios for the login feature.
    Verifications are about checking the title after login.
    The browser type is determined by supplying short name like 'chrome' or 'ff' or 'firefox'.
    The tests call the Driver_Factory class. Currently only local drivers are available.
    After obtaining a driver object, we call the Page_Factory class, which return a required page object.
    """
    log = customLogger(logging.DEBUG)

    def test_happpy_path_login(self):
        """
        Tests login feature. Providing valid username and password enables user to log in.
        """
        driver_object = Driver_Factory()
        driver = driver_object.get_web_driver("ff")
        # driver.maximize_window()

        login_object = Page_Factory.get_page_object("login", driver)

        if (login_object.login()):
            msg = "Login was successful"
            login_object.log.info(msg)
        else:
            msg = "Login failed"
            login_object.log.info(msg)

        time.sleep(3)
        login_object.verify_that_logged_in()

