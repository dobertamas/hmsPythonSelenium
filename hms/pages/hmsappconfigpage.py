import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import HmsAppConfigPageLocators
from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class HmsAppConfigPage(BasePage):
    """
    Page Object Model for the HMS Admin AppConfig page.
    Methods:
        start: to visit the page this class is modeling, using the inherited (fom BasePage) open method
    """
    log = custom_logger(logging.DEBUG)

    def start(self):
        """
        The start method also verifies the page title after getting the url.
        """
        self.url = '/hmsappconfig/list'
        self.open(self.url)
        self.log.info("Starting the HMS App Config page ")
        self.assertIn("HMS: HMSAppConfig", self._driver.title)

    def verify_table_first_column(self):
        self.isElementPresent(HmsAppConfigPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")

        element = self.getElement(HmsAppConfigPageLocators.TABLE_FIRST_COLUMN_USER_ID, "xpath")
        self.assertEqual(config.LOCAL_TDOBER['TABLE_FIRST_COLUMN_TEXT'].strip("\n"), element.text)
        return element.text

    def verify_table_second_column(self):
        self.isElementPresent(HmsAppConfigPageLocators.TABLE_SECOND_COLUMN_USER_ID, "xpath")

        element = self.getElement(HmsAppConfigPageLocators.TABLE_SECOND_COLUMN_USER_ID, "xpath")
        self.assertEqual(config.LOCAL_TDOBER['TABLE_SECOND_COLUMN_TEXT'].strip("\n"), element.text)
        return element.text
