class LoginPageLocators:
    LOGIN_LINK = "Login"
    USERNAME_FIELD = "username"
    PASSWORD_FIELD = "password"
    LOGIN_BUTTON = "signin"


class MainPageLocators:
    ACTIVE_CLASS = '//li[@class="active"]'
    ACTIVE_CLASS_CONTAINS = "//li[contains(text(),'Global Preferences')]"


class LocalRecTeamMemberAdminPageLocators:
    TABLE_FIRST_COLUMN_USER_ID = '//*[@id="dataTable"]/thead/tr[2]/th[1]'


class HmsAppConfigPageLocators:
    TABLE_FIRST_COLUMN_USER_ID = '//*[@id="dataTable"]/thead/tr[2]/th[1]'
    TABLE_SECOND_COLUMN_USER_ID = '//*[@id="dataTable"]/thead/tr[2]/th[2]'


class FindMemberPageLocators:
    MEMBER_ID_FIELD = 'memberId'
    FETCH_BUTTON = '//*[@id="crudform"]/div[2]/button'
