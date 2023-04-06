from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.GoogleFit.pages.commons.continue_as_page_base import ContinueAsPageBase
from selenium.webdriver import Remote


class ContinueAsPage(ContinueAsPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__fit_app_logo = (AppiumBy.ID, "com.google.android.apps.fitness:id/fit_app_icon")
        self.__continue_as_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/login_button")

    def click_continue_as_button(self):
        self.driver.find_element(self.__continue_as_button[0], self.__continue_as_button[1]).click()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(self.__fit_app_logo[0], self.__fit_app_logo[1]).is_displayed() \
            and self.driver.find_element(self.__continue_as_button[0], self.__continue_as_button[1]).is_displayed()