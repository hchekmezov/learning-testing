from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.pages.commons.plans_page.log_workout_page_base import LogWorkoutPageBase
from src.mobile.utils.mobile_utils import *


class LogWorkoutPage(LogWorkoutPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "/android.widget.TextView[@text='Log Workout']")
        self.__checkmark = (AppiumBy.ACCESSIBILITY_ID, "Done")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__checkmark)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title))

    def click_checkmark(self):
        self.driver.find_element(*self.__checkmark).click()
