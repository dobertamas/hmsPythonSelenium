import logging
import unittest

from hms.pages.driver_factory import Driver_Factory
from hms.pages.page_factory import Page_Factory
from hms.utilities.custom_logger import customLogger


class Login_Tests(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    def test_happpy_path_login(self):
        driver_object = Driver_Factory()
        driver = driver_object.get_web_driver("ff")
        #driver.maximize_window()

        login_object = Page_Factory.get_page_object("login", driver)

        if (login_object.login()):
            msg = "Login was successful"
            result_flag = True
            login_object.log.info(msg)
        else:
            msg = "Login failed"
            login_object.log.info(msg)
