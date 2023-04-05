from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.pages.commons.login_page_base import LoginPageBase


class LoginPage(LoginPageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.__email_field = (AppiumBy.ID, "com.myfitnesspal.android:id/email_address_edit")
        self.__password_field = (AppiumBy.ID, "com.myfitnesspal.android:id/password_edit")
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/login_button")

    def type_email_and_password(self, email, password):
        self.driver.find_element(self.__email_field[0], self.__email_field[1]).send_keys(email)
        self.driver.find_element(self.__password_field[0], self.__password_field[1]).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(self.__login_button[0], self.__login_button[1]).click()

    def is_login_button_enabled(self):
        return self.driver.find_element(self.__login_button[0], self.__login_button[1]).is_enabled()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(self.__email_field[0], self.__email_field[1]).is_displayed() \
        and self.driver.find_element(self.__password_field[0], self.__password_field[1]).is_displayed()