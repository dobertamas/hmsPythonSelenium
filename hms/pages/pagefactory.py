from hms.pages.loginpage import LoginPage
from hms.pages.mainpage import MainPage


class PageFactory:
    """ Returns the appropriate page object based on the name of the page """

    # TODO move out base_url; specify it dynamically
    @staticmethod
    def get_page_object(page_name, driver, base_url='http://localhost:8084/console/'):
        """Return the appropriate page object based on page_name
        :rtype: BasePage
        """

        test_page_object = None
        page_name = page_name.lower()
        if page_name == "login":
            test_page_object = LoginPage(driver, base_url=base_url)
        elif page_name == "main":
            test_page_object = MainPage(driver, base_url=base_url)

        return test_page_object
