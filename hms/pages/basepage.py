import logging
import unittest
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class BasePage(unittest.TestCase):
    """
    This class is serving basic attributes/functions for every single page inherited from it.
    Attributes:
        selenium_driver: allows you to drive the browser.
        base_url: The HMS Admin Console base URL unless passed in differently
    Methods:
        start: Page Object Model classes, extending BasePage, need to specify their own relative URL
        open: invokes the driver's get method to visit the page in question
    """
    log = custom_logger(logging.DEBUG)

    def __init__(self, selenium_driver, base_url=config.LOCAL_TDOBER['BASE_URL']):
        super().__init__()
        self._base_url = base_url
        self._driver = selenium_driver
        if self._driver is not None:
            self.start()

    def start(self):
        """
        Overwrite this method in your Page module to visit the given page's URL.
        Provide a relative URL there like '/config/list'
        """
        pass

    def open(self, url):
        """
        Provide a relative URL for this method in your Page module
        """
        url = self._base_url + url
        self._driver.get(url)

    """ 
    Webdriver-related methods to be used in Page modules 
    """

    def getElement(self, locator, strategy):
        """
        Receives the locator type (with other words, strategy) like By.NAME and
        uses the webdriver's find_element method. Returns the found WebElement. See doc at
        https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html?highlight=find_element#selenium.webdriver.remote.webdriver.WebDriver.find_element
        """
        element = None
        try:
            strategy = strategy.lower()
            by_type = self.getByType(strategy)
            element = self._driver.find_element(by_type, locator)
            self.log.debug("Element Found with locator: {} and  strategy: {}".format(locator, strategy))
        except NoSuchElementException:
            self.log.debug("Element not found with locator: " + locator + " and  strategy: " + strategy)
        return element

    def getByType(self, locator_type):
        """
        Helper method to find the appropriate Selenium locator strategy like By.NAME. See doc at
        https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.by.html?highlight=by#selenium.webdriver.common.by
        :param locator_type:
        :return: selenium.webdriver.common.by
        """
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "tag":
            return By.TAG_NAME
        else:
            self.log.debug("Locator type {} not correct/supported".format(locator_type))
        return False

    def sendKeys(self, data, locator, locator_type="name"):
        """
        After locating the WebElement we want to send some data, like entering username
        :param data: the actual data
        :param locator: from the LoginPageLocators class, where they are grouped by page
        :param locator_type: name or xpath or id etc.
        """
        try:
            element = self.getElement(locator, locator_type)
            element.send_keys(data)
            self.log.debug(
                "Sent data {} with locator: {} and locatorType: {} ".format(data, locator, locator_type))
        except ElementNotVisibleException:
            self.log.debug("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def elementClick(self, locator, locator_type="name"):
        """
        After locating a button we want to click on it
        :param locator: from the LoginPageLocators class, where they are grouped by page
        :param locator_type: name or xpath or id etc.
        """
        try:
            element = self.getElement(locator, locator_type)
            element.click()
            self.log.debug("Clicked on element with locator: {} and locator_type: {} ".format(locator, locator_type))
        except ElementNotVisibleException:
            self.log.debug(
                "Cannot click on the element with locator: {} and locator_type: {}".format(locator, locator_type))
            print_stack()

    def isElementPresent(self, locator, locator_type="id"):
        """
        Verifying that webdriver can locate the element on the page
        :param locator: from the LoginPageLocators class, where they are grouped by page
        :param locator_type: name or xpath or id etc.
        :return: True or False
        """
        try:
            element = self.getElement(locator, locator_type)
            if element is not None:
                self.log.debug("Element {} was found".format(element.text))
                return True
            else:
                self.log.debug("Element for locator {} was not found".format(locator))
                return False
        except NoSuchElementException:
            self.log.debug("Element was not found")
            return False

    def waitForElement(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        """
        Method to perform intelligent waits. It tries to find the element with a specified frequency.
        :param locator: from the LoginPageLocators class, where they are grouped by page
        :param locator_type: name or xpath or id etc.
        :param timeout: in seconds
        :param poll_frequency: in seconds
        :return: element
        """
        element = None
        try:
            by_type = self.getByType(locator_type)
            self.log.debug("Waiting for maximum :: " + str(timeout) +
                           " :: seconds for element to be clickable")
            wait = WebDriverWait(self._driver, timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(expected_conditions.element_to_be_clickable((by_type, locator)))
            self.log.debug("Element appeared on the web page")
        except NoSuchElementException:
            self.log.debug("Element not appeared on the web page")
            print_stack()
        return element
