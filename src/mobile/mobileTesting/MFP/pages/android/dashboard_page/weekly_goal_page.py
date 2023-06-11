from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.dashboard_page.weekly_goal_items import WeeklyGoalItem
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.weekly_goal_page_base import WeeklyGoalPageBase


class WeeklyGoalPage(WeeklyGoalPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/title_template")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")
        self.__needed_option = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__set_button))

    def set_weekly_goal(self, goal: WeeklyGoalItem):
        self.__needed_option = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/text' and "
                                                "@text='{}']/preceding-sibling::android.widget.RadioButton"
                                .format(goal.value))
        self.driver.find_element(*self.__needed_option).click()
        self.driver.find_element(*self.__set_button).click()

