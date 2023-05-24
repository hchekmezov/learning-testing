from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.privacy_center_items import PrivacyCenterItem

from src.mobile.mobileTesting.MFP.pages.commons.more_page.privacy_center_page_base import PrivacyCenterPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

class PrivacyCenterPage(PrivacyCenterPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "//*[@text='Privacy Center']")
        self.__back_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                             "/android.widget.ImageButton")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def click_privacy_center_option(self, option: PrivacyCenterItem) -> AbstractPage:
        self.driver.find_element(AppiumBy.ID, option.get_id()).click()
        return init_page_or_uiobject(self.driver, option.get_base_class())

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()
