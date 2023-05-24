from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.enums.more_page.newsfeed_sharing_items import NewsfeedSharingItem
from src.mobile.mobileTesting.MFP.pages.commons.more_page.newsfeed_sharing_page_base import NewsfeedSharingPageBase
from src.mobile.utils.mobile_utils import *

class NewsfeedSharingPage(NewsfeedSharingPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "//*[@text='News Feed Sharing']")
        self.__back_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                              "/android.widget.ImageButton")
        self.__option_for_verify = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def is_option_checked(self, option: NewsfeedSharingItem) -> bool:
        self.__option_for_verify = (AppiumBy.XPATH,
                                  "//*[@resource-id='com.myfitnesspal.android:id/chkDescription' "
                                  "and @text='{}']".format(option.value))
        if self.driver.find_element(*self.__option_for_verify).get_attribute('checked') == 'true':
            return True
        else:
            return False

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()

    def check_option(self, option: NewsfeedSharingItem):
        if self.is_option_checked(option):
            logger.info("[Newsfeed Sharing Page] Option {} already checked!".format(option))
        else:
            self.driver.find_element(*self.__option_for_verify).click()

    def uncheck_option(self, option: NewsfeedSharingItem):
        if not self.is_option_checked(option):
            logger.info("[Newsfeed Sharing Page] Option {} already unchecked!".format(option))
        else:
            self.driver.find_element(*self.__option_for_verify).click()
