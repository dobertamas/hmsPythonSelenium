import unittest


class Base_Page(unittest.TestCase):
    def __init__(self, selenium_driver, base_url='http://localhost:8084/console/'):
        self.base_url = base_url
        self.driver = selenium_driver
