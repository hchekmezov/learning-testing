from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.dashboard_page.activity_level import ActivityLevel
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.acitivity_level_page_base import ActivityLevelPageBase
from src.mobile.utils.mobile_utils import EC


class ActivityLevelPage(ActivityLevelPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")
        self.__needed_option = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__set_button))

    def set_activity_level(self, level: ActivityLevel):
        self.__needed_option = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/text1' "
                                                "and @text='{}']/../preceding-sibling::android.widget.RadioButton"
                                .format(level.value))
        self.driver.find_element(*self.__needed_option).click()
        self.driver.find_element(*self.__set_button).click()

