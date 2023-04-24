from appium.webdriver import Remote

from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.utils.device_type import *


# @device_type(page_type=DeviceType.IOS_PHONE, parent_class=MFPCommonPageBase)
class MFPCommonPage(MFPCommonPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    def wait_until_spinner_rounding(self):
        pass

    def get_bottom_nav_bar(self):
        pass

    def is_page_opened(self) -> bool:
        pass