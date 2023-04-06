from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.android.bottom_nav_container import BottomNavContainer
from src.mobile.mobileTesting.GoogleFit.pages.commons.gf_common_page_base import GFCommonPageBase


class GFCommonPage(GFCommonPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    def get_bottom_nav_container(self):
        return BottomNavContainer(self.driver)
