from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.commons.bottom_nav_bar_base import BottomNavBarBase

from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class BottomNavBar(BottomNavBarBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__class_nav_bar_item = None
        self.__nav_bar_view_group = (AppiumBy.XPATH, "//android.widget.FrameLayout"
                                                     "[@resource-id='com.myfitnesspal.android:id/bottomNavigationBar']"
                                                     "/android.view.ViewGroup")

    def click_on_nav_bar_item(self, nav_bar_item: BottomNavBarItem) -> AbstractPage:
        self.__class_nav_bar_item = (AppiumBy.ID, "com.myfitnesspal.android:id/action_{}"
                                     .format(nav_bar_item.get_button_name().lower()))
        self.driver.find_element(*self.__class_nav_bar_item).click()
        return init_page_or_uiobject(self.driver, nav_bar_item.get_base_class())

    def is_nav_bar_item_clickable(self, nav_bar_item: BottomNavBarItem):
        self.__class_nav_bar_item = (AppiumBy.ID, "com.myfitnesspal.android:id/action_{}"
                                     .format(nav_bar_item.get_button_name().lower()))
        if self.driver.find_element(*self.__class_nav_bar_item).get_attribute("clickable") == 'false':
            return False
        else:
            return True

    def is_present(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__nav_bar_view_group))
