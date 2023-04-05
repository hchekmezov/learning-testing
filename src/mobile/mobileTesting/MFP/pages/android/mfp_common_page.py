from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Remote

from src.mobile.mobileTesting.MFP.pages.android.bottom_nav_bar import BottomNavBar
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.constants import Constants


class MFPCommonPage(MFPCommonPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)


    def wait_until_spinner_rounding(self):
        # self.wait = WebDriverWait(self.driver, Constants.THIRTY_SECONDS.value)
        return self.wait.until(EC.invisibility_of_element_located((AppiumBy.ID, "com.myfitnesspal.android:id/progressPleaseWait")))

    def get_bottom_nav_bar(self):
        return BottomNavBar(self.driver)
