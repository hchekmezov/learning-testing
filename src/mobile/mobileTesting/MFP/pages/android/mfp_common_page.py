from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.bottom_nav_bar_base import BottomNavBarBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject


class MFPCommonPage(MFPCommonPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def wait_until_spinner_rounding(self):
        return WebDriverWait(self.driver, 30)\
            .until(EC.invisibility_of_element_located((AppiumBy.ID, "com.myfitnesspal.android:id/progressPleaseWait")))

    def get_bottom_nav_bar(self):
        bottom_nav_bar = init_page_or_uiobject(self.driver, BottomNavBarBase)
        if bottom_nav_bar.is_present():
            return bottom_nav_bar
        else:
            raise NoSuchElementException("[MFP Common Page] Bottom Nav Bar is not present!")
