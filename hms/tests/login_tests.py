import unittest

from hms.pages.driver_factory import Driver_Factory
from hms.pages.page_factory import Page_Factory


class Login_Tests(unittest.TestCase):

    def test_happpy_path_login(self):
        driver_object = Driver_Factory()
        driver = driver_object.get_web_driver("ff")

        driver.maximize_window()
        login_object = Page_Factory.get_page_object("login", driver)
