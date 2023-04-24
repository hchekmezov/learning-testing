from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver import Remote

from src.mobile.mobileTesting.MFP.pages.commons.bottom_nav_bar_base import BottomNavBarBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.constants import Constants
from src.mobile.utils.device_type import *
from src.mobile.utils.initialize_utils import init_page_or_uiobject


# @device_type(page_type=DeviceType.ANDROID_PHONE, parent_class=MFPCommonPageBase)
class MFPCommonPage(MFPCommonPageBase):

    # __annotations__ = {"pageType": "DeviceType.Type.ANDROID_PHONE", "parentClass": "MFPCommonPageBase.class"}

    def __init__(self, driver: Remote):
        super().__init__(driver)



    def wait_until_spinner_rounding(self):
        # self.wait = WebDriverWait(self.driver, Constants.THIRTY_SECONDS.value)
        return self.wait.until(EC.invisibility_of_element_located((AppiumBy.ID, "com.myfitnesspal.android:id/progressPleaseWait")))

    def get_bottom_nav_bar(self):
        return init_page_or_uiobject(self.driver, BottomNavBarBase)
