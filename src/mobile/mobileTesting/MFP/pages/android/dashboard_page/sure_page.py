from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.sure_page_base import SurePageBase
from src.mobile.utils.mobile_utils import EC


class SurePage(SurePageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__yes_button = (AppiumBy.ID, "android:id/button1")
        self.__no_button = (AppiumBy.ID, "android:id/button2")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__yes_button))

    def click_yes_button(self):
        self.driver.find_element(*self.__yes_button).click()

    def click_no_button(self):
        self.driver.find_element(*self.__no_button).click()


