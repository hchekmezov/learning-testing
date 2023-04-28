from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.custom_summary_item import CustomSummaryItem
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_summary_page_base import CustomSummaryPageBase
from src.mobile.utils.mobile_utils import *


class CustomSummaryPage(CustomSummaryPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__nutrient_by_short_version = None
        self.__save_button = (AppiumBy.ACCESSIBILITY_ID, "Done")
        self.__nutrient_selected_text = (AppiumBy.ID, "com.myfitnesspal.android:id/tvNutrientSelected")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__save_button))

    def check_nutrient(self, summary_item: CustomSummaryItem):
        self.__nutrient_by_short_version = (AppiumBy.ID, "com.myfitnesspal.android:id/cb{}"
                                            .format(summary_item.get_short_version()))
        if swipeToElementVerticalWithCount(self.__nutrient_by_short_version, 5, self.driver, OS.ANDROID):
            if not self.is_nutrient_checked(summary_item):
                self.driver.find_element(*self.__nutrient_by_short_version).click()
            else:
                logger.info("Element already checked! No need to check it!")
        else:
            raise NoSuchElementException()

    def uncheck_nutrient(self, summary_item: CustomSummaryItem):
        self.__nutrient_by_short_version = (AppiumBy.ID, "com.myfitnesspal.android:id/cb{}"
                                            .format(summary_item.get_short_version()))
        if swipeToElementVerticalWithCount(self.__nutrient_by_short_version, 5, self.driver, OS.ANDROID):
            if self.is_nutrient_checked(summary_item):
                self.driver.find_element(*self.__nutrient_by_short_version).click()
            else:
                logger.info("Element already unchecked! No need to uncheck it!")
        else:
            raise NoSuchElementException()

    def is_nutrient_checked(self, summary_item: CustomSummaryItem) -> bool:
        self.__nutrient_by_short_version = (AppiumBy.ID, "com.myfitnesspal.android:id/cb{}"
                                            .format(summary_item.get_short_version()))
        if swipeToElementVerticalWithCount(self.__nutrient_by_short_version, 5, self.driver, OS.ANDROID):
            is_checked = self.driver.find_element(*self.__nutrient_by_short_version).get_attribute("checked")
            if is_checked == 'true':
                return True
            else:
                return False
        else:
            raise NoSuchElementException()

    def is_save_button_active(self) -> bool:
        is_active = self.driver.find_element(*self.__save_button).get_attribute('enabled')
        if is_active == 'true':
            return True
        else:
            return False

    def get_nutrient_selected_text(self) -> str:
        # self.driver.implicitly_wait(2)
        swipeToElementVerticalWithCount(self.__nutrient_selected_text, 7, self.driver, OS.ANDROID)
        return self.driver.find_element(*self.__nutrient_selected_text).text








