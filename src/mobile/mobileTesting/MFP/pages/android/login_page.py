from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import Remote

from src.mobile.mobileTesting.MFP.pages.commons.existing_user_tutor_page_base import ExistingUserTutorPageBase
from src.mobile.mobileTesting.MFP.pages.commons.login_page_base import LoginPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject


class LoginPage(LoginPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__email_field = (AppiumBy.ID, "com.myfitnesspal.android:id/email_address_edit")
        self.__password_field = (AppiumBy.ID, "com.myfitnesspal.android:id/password_edit")
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/login_button")

    def type_email_and_password(self, email, password):
        self.driver.find_element(*self.__email_field).send_keys(email)
        self.driver.find_element(*self.__password_field).send_keys(password)

    def click_login_button(self) -> ExistingUserTutorPageBase:
        self.driver.find_element(*self.__login_button).click()
        assert init_page_or_uiobject(self.driver, MFPCommonPageBase).wait_until_spinner_rounding(), \
            "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
        return init_page_or_uiobject(self.driver, ExistingUserTutorPageBase)

    def is_login_button_enabled(self):
        return self.driver.find_element(*self.__login_button).is_enabled()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__email_field).is_displayed() \
        and self.driver.find_element(*self.__password_field).is_displayed()