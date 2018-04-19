import logging
import unittest
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from hms.utilities.custom_logger import custom_logger


class BasePage(unittest.TestCase):
    """
    This class is serving basic attributes/functions for every single page inherited from it.
    Attributes:
        selenium_driver: allows you to drive the browser.
        base_url: The HMS Admin Console base URL unless passed in differently
    Methods:
        start:


    """
    log = custom_logger(logging.DEBUG)

    def __init__(self, selenium_driver, base_url='http://localhost:8084/console'):
        super().__init__()
        self._base_url = base_url
        self._driver = selenium_driver
        if self._driver is not None:
            self.start()

    """ 
    Overwrite this method in your Page module to visit the given page's URL.
    Provide a relative URL there like '/config/list' 
    """

    def start(self):
        pass

    """ 
    Provide a relative URL for this method in your Page module 
    """

    def open(self, url):
        url = self._base_url + url
        self._driver.get(url)

    """ 
    Webdriver-related methods to be used in Page modules 
    """

    def getElement(self, locator, locator_type):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.getByType(locator_type)
            element = self._driver.find_element(by_type, locator)
            self.log.debug("Element Found with locator: " + locator + " and  locatorType: " + locator_type)
        except NoSuchElementException:
            self.log.debug("Element not found with locator: " + locator + " and  locatorType: " + locator_type)
        return element

    def getByType(self, locator_type):
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
            self.log.debug("Locator type " + locator_type + " not correct/supported")
        return False

    def sendKeys(self, data, locator, locator_type="name"):
        try:
            element = self.getElement(locator, locator_type)
            element.send_keys(data)
            self.log.debug("Sent data on element with locator: " + locator + " locatorType: " + locator_type)
        except ElementNotVisibleException:
            self.log.debug("Cannot send data on the element with locator: " + locator +
                           " locatorType: " + locator_type)
            print_stack()

    def elementClick(self, locator, locator_type="name"):
        try:
            element = self.getElement(locator, locator_type)
            # time.sleep(3)
            element.click()
            self.log.debug("Clicked on element with locator: " + locator + " locator_type: " + locator_type)
        except ElementNotVisibleException:
            self.log.debug("Cannot click on the element with locator: " + locator + " locator_type: " + locator_type)
            print(" could not click ")
            print_stack()

    def isElementPresent(self, locator, locator_type="id"):
        try:
            element = self.getElement(locator, locator_type)
            if element is not None:
                self.log.debug("Element Found")
                return True
            else:
                self.log.debug("Element not found")
                return False
        except NoSuchElementException:
            self.log.debug("Element not found")
            return False

    def waitForElement(self, locator, locator_type="id",
                       timeout=10, poll_frequency=0.5):
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
