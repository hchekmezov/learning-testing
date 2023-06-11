from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.more_page.height_page_base import HeightPageBase


class HeightPage(HeightPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")
        self.__text_height = (AppiumBy.ID, "com.myfitnesspal.android:id/txtHeight")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__set_button))

    def set_height(self, height: int):
        # height_edit_elem = self.driver.find_element(*self.__text_height)

        self.driver.find_element(*self.__text_height).clear().send_keys(str(height))

        self.driver.find_element(*self.__set_button).click()



