from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.direction import *
from src.mobile.utils.operating_system import OS



class DashboardPage(DashboardPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__user_avatar = (AppiumBy.ACCESSIBILITY_ID, "User avatar")
        self.__track_steps_button = (AppiumBy.XPATH, "//android.view.View[@content-desc='Progress steps card']"
                                                          "/android.view.View/android.widget.Button")
        self.__bottom_horizontal_container = (AppiumBy.XPATH, "(//android.view.View"
                                                              "[@content-desc='Dashboard horizontal pager'])[2]")
    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__user_avatar))  \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase)\
                .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.DASHBOARD)

    def click_track_steps_button(self):
        swipeUp(500, 2, self.driver, OS.ANDROID)

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

    def click_user_avatar(self) -> UserPageBase:
        self.driver.find_element(*self.__user_avatar).click()
        return init_page_or_uiobject(self.driver, UserPageBase)





