from hms.pages.localrecteammemberadminpage import LocalRecTeamMemberAdminPage
from hms.pages.loginpage import LoginPage
from hms.pages.mainpage import MainPage
from hms.utilities import config


class PageFactory:
    """
    Returns the appropriate page object based on the name of the page.
    The browser type is determined by supplying short name like 'chrome' or 'ff' or 'firefox'.
    The tests call the Driver_Factory class. Currently only local drivers are available.
    After obtaining a driver object, we call the Page_Factory class, which returns a required page object.
    """

    @staticmethod
    def get_page_object(page_name, driver, base_url=config.LOCAL_TDOBER['BASE_URL']):
        """Return the appropriate page object based on page_name
        :rtype: BasePage
        """

        test_page_object = None
        if page_name == "login":
            test_page_object = LoginPage(driver, base_url=base_url)
        elif page_name == "main":
            test_page_object = MainPage(driver, base_url=base_url)
        elif page_name == "teammemberadmin":
            test_page_object = LocalRecTeamMemberAdminPage(driver, base_url=base_url)

        return test_page_object
