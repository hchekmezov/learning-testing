from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.newsfeed_page_base import NewsfeedPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class NewsfeedPage(NewsfeedPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.widget.LinearLayout"
                                        "[@resource-id='com.myfitnesspal.android:id/toolbar_container']"
                                        "//android.widget.TextView")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and not init_page_or_uiobject(self.driver, MFPCommonPageBase) \
            .get_bottom_nav_bar().is_nav_bar_item_clickable(BottomNavBarItem.NEWSFEED)