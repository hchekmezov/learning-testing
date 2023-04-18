from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.colors import Color
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.commons.profile_pages.settings_page_base import SettingsPageBase
from src.mobile.utils.mobile_utils import *


class SettingsPage(SettingsPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@text='Settings']")
        self.__back_button = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.wait.until(EC.visibility_of_element_located(self.__back_button))

    def color_of_title(self, title_text):
        locator = (AppiumBy.XPATH, "//*[@resource-id='android:id/title' and @text='{}']".format(title_text))
        swipeToElementWithCount(locator, 10, self.driver, OS.ANDROID)
        return GFCommonPage(self.driver).get_color_of_element(locator)






