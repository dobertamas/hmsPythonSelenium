from selenium import webdriver


class DriverFactory:
    """
    Class to create and return a Selenium webdriver.
    Attributes:
        browser(str): The name of the browser. Currently it can be firefox or ff.
        browser_version (str): The version number of the browser. Currently unused.
    Methods: run_local(browser): Depending on the browser type, different setup tests are required.
        Please note that future versions of browsers might require an updated version of geckodriver,
        which should be installed on the host before starting Selenium testing.

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
            # TODO set up chrome driver with webdriver
            # selenium.common.exceptions.SessionNotCreatedException: Message: Unable
            # to find a matching set of capabilities
            local_driver = webdriver.Chrome('/opt/geckodriver')
        elif browser.lower() == "opera":
            # TODO maybe set up opera driver with webdriver
            # 'operadriver' executable needs to be in PATH
            local_driver = webdriver.Opera()
        elif browser.lower() == "safari":
            # TODO set up safari driver with webdriver
            # AttributeError: 'WebDriver' object has no attribute 'service'
            local_driver = webdriver.Safari()
        return local_driver
