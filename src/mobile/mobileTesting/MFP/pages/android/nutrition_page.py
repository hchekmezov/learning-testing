from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.pages.commons.nutrition_page_base import NutritionPageBase
from src.mobile.utils.mobile_utils import *


class NutritionPage(NutritionPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "/android.widget.TextView[@text='Nutrition']")
        self.__mini_food_container = (AppiumBy.ID, "com.myfitnesspal.android:id/mini_food_list_container")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.driver.find_element(*self.__mini_food_container).is_displayed()