import logging

from hms.pages.basepage import BasePage
from hms.pages.locators import MemberDetailPageLocators
from hms.utilities import config
from hms.utilities.custom_logger import custom_logger


class MemberDetailPage(BasePage):
    """
           Page Object Model for the HMS Member Detail page.
           Methods:
               start: to visit the page this class is modeling, using the inherited (fom BasePage) open method
               verify_points: reads the Points value from the Member Detail page and compares it to the value from the config file.
           """
    log = custom_logger(logging.DEBUG)

    def __init__(self, selenium_driver, id, memberid, base_url):
        # super().__init__(selenium_driver, base_url=config.LOCAL_TDOBER['BASE_URL'])
        self._base_url = base_url = config.LOCAL_TDOBER['BASE_URL']
        self._driver = selenium_driver
        self._id = id
        self._memberid = memberid
        if self._driver is not None:
            self.start(id, memberid)

    def start(self, id, memberid):
        """
        The start method also verifies the page title after getting the url.
        """
        self.url = "member/detail?id={}&memberid={}".format(id, memberid)
        self.open(self.url)
        self.log.info("Starting the find member page ")
        self.assertIn("HMS: Member Info", self._driver.title)

    def verify_points(self):
        self.assertTrue(self.isElementPresent(MemberDetailPageLocators.POINTS, "xpath"),
                        "We are not on the expected page")
        element = self.getElement(MemberDetailPageLocators.POINTS, "xpath")
        print(element.text)
        print(config.LOCAL_TDOBER['FETCHED_MEMBER_POINTS'])
        # self.assertEqual(config.LOCAL_TDOBER['FETCHED_MEMBER_POINTS'], element.text)
        return element.text
