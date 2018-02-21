import logging
import time
import unittest
from traceback import print_stack

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from hms.utilities.custom_logger import customLogger


class Base_Page(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    def __init__(self, selenium_driver, base_url='http://localhost:8084/console'):
        self.base_url = base_url
        self.driver = selenium_driver
        if self.driver is not None:
            self.start()

    """ 
    Overwrite this method in your Page module to visit a specific URL 
    """
    def start(self):
        pass


    """ 
    Provide a relative URL for this method in your Page module 
    """
    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)


    """ 
    Webdriver-related methods to be used in Page modules 
    """
    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.debug("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.debug("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
        return element

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        else:
            self.log.debug("Locator type " + locatorType + " not correct/supported")
        return False

    def sendKeys(self, data, locator, locatorType="name"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.debug("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.debug("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def elementClick(self, locator, locatorType="name"):
        try:
            element = self.getElement(locator, locatorType)
            time.sleep(3)
            element.click()
            self.log.debug("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.debug("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print(" could not click ")
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.debug("Element Found")
                return True
            else:
                self.log.debug("Element not found")
                return False
        except:
            self.log.debug("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                       timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.debug("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(expected_conditions.element_to_be_clickable((byType, locator)))
            self.log.debug("Element appeared on the web page")
        except:
            self.log.debug("Element not appeared on the web page")
            print_stack()
        return element
