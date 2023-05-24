from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.more_page.more_menu_options import MoreMenuOption
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.more_page_base import MorePageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *


class MorePage(MorePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__user_name = (AppiumBy.ID, "com.myfitnesspal.android:id/user_name")
        self.__option = None

    def is_page_opened(self) -> bool:
        return swipeToElementVerticalDownFirstWithCountAndDuration(self.__user_name, 5, 600, self.driver, OS.ANDROID) \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase) \
                .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.MORE)

    def is_option_present(self, option: MoreMenuOption) -> bool:
        self.__option = (AppiumBy.XPATH, "//*[@text='{}']".format(option.get_text()))
        return swipeToElementVerticalWithCount(self.__option, 7, self.driver, OS.ANDROID)

    def click_option(self, option: MoreMenuOption) -> AbstractPage:
        if self.is_option_present(option):
            self.driver.find_element(*self.__option).click()
        return init_page_or_uiobject(self.driver, option.get_base_class())
