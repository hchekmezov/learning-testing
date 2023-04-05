from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
import logging
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from selenium.webdriver import Remote
from src.mobile.mobileTesting.MFP.pages.commons.bottom_nav_bar_base import BottomNavBarBase
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class BottomNavBar(BottomNavBarBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        # self.__dashboard = (AppiumBy.ACCESSIBILITY_ID, BottomNavBarItem.DASHBOARD.value)
        # self.__diary = (AppiumBy.ACCESSIBILITY_ID, BottomNavBarItem.DIARY.value)
        # self.__newsfeed = (AppiumBy.ACCESSIBILITY_ID, BottomNavBarItem.NEWSFEED.value)
        # self.__plans = (AppiumBy.ACCESSIBILITY_ID, BottomNavBarItem.PLANS.value)
        # self.__more = (AppiumBy.ACCESSIBILITY_ID, BottomNavBarItem.MORE.value)
        self.__nav_bar_item = None
        self.__nav_bar_view_group = (AppiumBy.XPATH, "//android.widget.FrameLayout"
                                                     "[@resource-id='com.myfitnesspal.android:id/bottomNavigationBar']"
                                                     "/android.view.ViewGroup")

    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem):
        self.__nav_bar_item = (AppiumBy.ACCESSIBILITY_ID, nav_bar_item.value)
        self.driver.find_element(self.__nav_bar_item[0], self.__nav_bar_item[1]).click()

    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem):
        self.__nav_bar_item = (AppiumBy.ACCESSIBILITY_ID, nav_bar_item.value)
        if self.driver.find_element(self.__nav_bar_item[0], self.__nav_bar_item[1]).get_attribute("clickable") == 'false':
            return False
        else:
            return True


    def is_present(self) -> bool:
        return self.driver.find_element(self.__nav_bar_view_group[0], self.__nav_bar_view_group[1]).is_displayed()