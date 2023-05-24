from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.quick_add_page_base import QuickAddPageBase
from src.mobile.utils.mobile_utils import *


class QuickAddPage(QuickAddPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@text='Quick Add']")
        self.__done_button = (AppiumBy.ACCESSIBILITY_ID, "Done")
        self.__fat_field = (AppiumBy.ID, "com.myfitnesspal.android:id/tvQuickFat")
        self.__carbs_field = (AppiumBy.ID, "com.myfitnesspal.android:id/tvQuickCarbs")
        self.__protein_field = (AppiumBy.ID, "com.myfitnesspal.android:id/tvQuickProtein")
        self.__calories_field = (AppiumBy.ID, "com.myfitnesspal.android:id/tvQuickCalories")

        self.__no_thanks_button = (AppiumBy.ACCESSIBILITY_ID, "NO THANKS")

    def is_page_opened(self) -> bool:
        self.driver.hide_keyboard()
        self.driver.implicitly_wait(5)
        # logger.info(self.driver.find_elements(*self.__no_thanks_button))
        if bool(self.driver.find_element(*self.__no_thanks_button).is_displayed()):
            self.driver.find_element(*self.__no_thanks_button).click()
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__done_button))

    def quick_add_fat_carbs_protein(self, fat: int, carbs: int, protein: int):
        self.driver.hide_keyboard()
        self.driver.find_element(*self.__fat_field).send_keys(str(fat))
        self.driver.find_element(*self.__carbs_field).send_keys(str(carbs))
        self.driver.find_element(*self.__protein_field).send_keys(str(protein))

    def is_calories_equals_value(self, value: int) -> bool:
        return int(self.driver.find_element(*self.__calories_field).text) == value
