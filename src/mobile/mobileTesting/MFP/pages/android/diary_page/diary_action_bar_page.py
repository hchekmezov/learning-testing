from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_action_bar_page_base import DiaryActionBarPageBase
from src.mobile.utils.mobile_utils import EC


class DiaryActionBarPage(DiaryActionBarPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__move_to = (AppiumBy.XPATH, "//*[@text='Move to…']/..")
        self.__delete_entry = (AppiumBy.XPATH, "//*[@text='Delete Entry']/..")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__move_to)) and \
            self.wait.until(EC.visibility_of_element_located(self.__delete_entry))

    def click_delete_entry(self):
        self.driver.find_element(*self.__delete_entry).click()

