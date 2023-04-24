from appium.webdriver.common.appiumby import AppiumBy
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.commons.bottom_nav_bar_base import BottomNavBarBase

from typing import Union

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page_base import MorePageBase
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page_base import NewsfeedPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page_base import PlansPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

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
        self.__class_nav_bar_item = None
        self.__nav_bar_view_group = (AppiumBy.XPATH, "//android.widget.FrameLayout"
                                                     "[@resource-id='com.myfitnesspal.android:id/bottomNavigationBar']"
                                                     "/android.view.ViewGroup")

    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem) -> Union[DashboardPageBase, DiaryPageBase,
                                                                        NewsfeedPageBase, PlansPageBase, MorePageBase]:
        self.__class_nav_bar_item = (AppiumBy.ACCESSIBILITY_ID, nav_bar_item.get_button_name())
        self.driver.find_element(*self.__class_nav_bar_item).click()
        return init_page_or_uiobject(self.driver, nav_bar_item.get_base_class())

    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem):
        self.__class_nav_bar_item = (AppiumBy.ACCESSIBILITY_ID, nav_bar_item.get_button_name())
        if self.driver.find_element(*self.__class_nav_bar_item).get_attribute("clickable") == 'false':
            return False
        else:
            return True


    def is_present(self) -> bool:
        # return self.driver.find_element(*self.__nav_bar_view_group).is_displayed()
        return self.wait.until(EC.visibility_of_element_located(self.__nav_bar_view_group))