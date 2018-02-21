import logging
import time
import unittest
from traceback import print_stack

from selenium.webdriver.common.by import By

from hms.utilities.custom_logger import customLogger


class Base_Page(unittest.TestCase):
    log = customLogger(logging.DEBUG)

    def __init__(self, selenium_driver, base_url='http://localhost:8084/console'):
        self.base_url = base_url
        self.driver = selenium_driver
        if self.driver is not None:
            self.start()

    def start(self):
        "Overwrite this method in your Page module if you want to visit a specific URL"
        pass

    def open(self, url):
        "Visit the page base_url + url"
        url = self.base_url + url
        self.driver.get(url)

    def sendKeys(self, data, locator, locatorType="name"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def getElement(self, locator, locatorType):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator + " and  locatorType: " + locatorType)
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
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def elementClick(self, locator, locatorType="name"):
        try:
            element = self.getElement(locator, locatorType)
            time.sleep(4)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
            print(" clicked ")
        except:
            self.log.info("Cannot click on the element with locator: " + locator + " locatorType: " + locatorType)
            print(" could not click ")
            print_stack()
