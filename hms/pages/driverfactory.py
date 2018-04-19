from selenium import webdriver


class DriverFactory:
    """
    Class to create and return a Selenium webdriver.

    Attributes:
        browser(str): The name of the browser. Currrently it can be firefox or ff
    """

    def __init__(self, browser='ff', browser_version=None):
        self.browser_version = browser_version
        self.browser = browser

    def get_web_driver(self, browser):
        web_driver = self.run_local(browser)
        return web_driver

    @staticmethod
    def run_local(browser):
        local_driver = None
        if browser.lower() == "ff" or browser.lower() == 'firefox':
            local_driver = webdriver.Firefox()
            print("")
        elif browser.lower() == "chrome":
            # selenium.common.exceptions.SessionNotCreatedException: Message: Unable
            # to find a matching set of capabilities
            # cap = {'binary_location': '/opt/geckodriver'}
            # cap["marionette"] = False
            # local_driver = webdriver.Chrome(desired_capabilities=cap, executable_path='/opt/geckodriver')
            local_driver = webdriver.Chrome('/opt/geckodriver')
        elif browser.lower() == "opera":
            # 'operadriver' executable needs to be in PATH
            local_driver = webdriver.Opera()
        elif browser.lower() == "safari":
            # AttributeError: 'WebDriver' object has no attribute 'service'
            local_driver = webdriver.Safari()

        return local_driver
