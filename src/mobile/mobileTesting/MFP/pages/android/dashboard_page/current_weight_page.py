from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.current_weight_page_base import CurrentWeightPageBase


class CurrentWeightPage(CurrentWeightPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__edit_text_field = (AppiumBy.ID, "com.myfitnesspal.android:id/txtValue")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__cancel_button))

    def set_weight(self, weight: int):
        self.driver.find_element(*self.__edit_text_field).clear().send_keys(str(weight))
        self.driver.find_element(*self.__set_button).click()

