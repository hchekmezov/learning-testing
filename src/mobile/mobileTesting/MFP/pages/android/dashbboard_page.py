from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.android.mfp_common_page import MFPCommonPage
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.direction import *
from src.mobile.utils.operating_system import OS



class DashboardPage(DashboardPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__user_avatar = (AppiumBy.XPATH, "//android.view.View[@content-desc='User avatar']")
        self.__track_steps_button = (AppiumBy.XPATH, "//android.view.View[@content-desc='Progress steps card']"
                                                          "/android.view.View/android.widget.Button")
        self.__bottom_horizontal_container = (AppiumBy.XPATH, "(//android.view.View"
                                                              "[@content-desc='Dashboard horizontal pager'])[2]")
    #     self.__weight_card = (AppiumBy.ACCESSIBILITY_ID, "Progress weight card")
    def is_page_opened(self) -> bool:
        return self.driver.find_element(self.__user_avatar[0], self.__user_avatar[1]).is_displayed()  \
            and not MFPCommonPage(self.driver).get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.DASHBOARD)

    def click_track_steps_button(self):
        swipeUp(500, 2, self.driver, OS.ANDROID)
        # swipeLeftInContainer(self.driver.find_element(self.__bottom_horizontal_container[0],
        #                                               self.__bottom_horizontal_container[1]),
        #                      100, self.driver, OS.ANDROID)

        # swipeInContainer(self.driver.find_element(self.__bottom_horizontal_container[0],
        #                                           self.__bottom_horizontal_container[1]),
        #                  Direction.LEFT, 2, 100, self.driver, OS.ANDROID)

        # swipeLeftInContainerWithCount(self.driver.find_element(self.__bottom_horizontal_container[0],
        #                                           self.__bottom_horizontal_container[1]),
        #                               100,
        #                               2,
        #                               self.driver,
        #                               OS.ANDROID)

        swipe(self.__track_steps_button, self.driver.find_element(self.__bottom_horizontal_container[0],
                                                  self.__bottom_horizontal_container[1]),
                           Direction.LEFT,
                           30,
                           100,
                           self.driver,
                           OS.ANDROID)

        assert self.driver.find_element(self.__track_steps_button[0], self.__track_steps_button[1]).is_displayed(), \
            "[Dashboard Page] Track Your Steps button not found!"
        self.driver.find_element(self.__track_steps_button[0], self.__track_steps_button[1]).click()



