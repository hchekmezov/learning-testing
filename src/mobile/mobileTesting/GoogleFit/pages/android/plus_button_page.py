from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.plus_button_page_item import PlusButtonPageItem
from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_page_base import PlusButtonPageBase


class PlusButtonPage(PlusButtonPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__page_dial_item_by_title = (
            AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/mtrl_internal_speed_dial_item']"
                            "//*[@text='{}']/..")
        self.__add_entry_speed_dial = (AppiumBy.ID, "com.google.android.apps.fitness:id/add_entry_speed_dial")
        self.__close_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/add_entry_fab")

    def click_item_on_page(self, item: PlusButtonPageItem):
        self.driver.find_element(self.__page_dial_item_by_title[0],
                                 self.__page_dial_item_by_title[1].format(item.value)).click()

    def is_page_opened(self) -> bool:
        return self.driver.find_element(*self.__add_entry_speed_dial).is_displayed() \
            and self.driver.find_element(*self.__close_button).is_displayed()

    def close_page(self):
        self.driver.find_element(*self.__close_button).click()

