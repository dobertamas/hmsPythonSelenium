from selenium import webdriver


class DriverFactory:

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
        elif browser.lower() == "ie":

            local_driver = webdriver.Ie()
        elif browser.lower() == "chrome":
            # cap = {'binary_location': '/opt/geckodriver'}
            # cap["marionette"] = False
            # local_driver = webdriver.Chrome(desired_capabilities=cap, executable_path='/opt/geckodriver')
            local_driver = webdriver.Chrome('/opt/geckodriver')
        elif browser.lower() == "opera":
            local_driver = webdriver.Opera()
        elif browser.lower() == "safari":
            local_driver = webdriver.Safari()

        return local_driver
