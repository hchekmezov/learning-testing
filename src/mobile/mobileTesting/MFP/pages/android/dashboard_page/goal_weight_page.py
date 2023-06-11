from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.goal_weight_page_base import GoalWeightPageBase


class GoalWeightPage(GoalWeightPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")
        self.__current_option = (AppiumBy.ID, "android:id/numberpicker_input")
        self.__top_button = (AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']"
                                             "/preceding-sibling::android.widget.Button")
        self.__bottom_button = (AppiumBy.XPATH, "//*[@resource-id='android:id/numberpicker_input']"
                                                "/following-sibling::android.widget.Button")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__cancel_button))

    def set_weight(self, weight: float):
        if float(self.driver.find_element(*self.__current_option).text) > weight:
            top_direction = True
        else:
            top_direction = False

        if top_direction:
            while self.driver.find_element(*self.__current_option).text != str(weight):
                self.driver.find_element(*self.__top_button).click()
        else:
            while self.driver.find_element(*self.__current_option).text != str(weight):
                self.driver.find_element(*self.__bottom_button).click()

        self.driver.find_element(*self.__set_button).click()

