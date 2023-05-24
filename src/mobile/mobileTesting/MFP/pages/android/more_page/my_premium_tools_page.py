from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.more_page.more_menu_options import MoreMenuOption
from src.mobile.mobileTesting.MFP.enums.my_prem_tools_items import MyPremToolsItem
from src.mobile.mobileTesting.MFP.pages.commons.more_page.my_premium_tools_page_base import MyPremiumToolsPageBase
from src.mobile.utils.mobile_utils import EC, swipeToElementVerticalWithCount
from src.mobile.utils.operating_system import OS


class MyPremiumToolsPage(MyPremiumToolsPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__header = (AppiumBy.ID, "com.myfitnesspal.android:id/tv_header_text")
        self.__needed_view_group = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__header)) \
            and self.driver.find_element(*self.__header).text == MoreMenuOption.MY_PREMIUM_TOOLS.get_text()

    def is_option_and_description_displayed(self, option: MyPremToolsItem) -> bool:
        self.__needed_view_group = (AppiumBy.XPATH,
                                    "//*[@resource-id='com.myfitnesspal.android:id/tv_desc' and @text='{}']/.."
                                    "/*[@resource-id='com.myfitnesspal.android:id/tv_header' and @text='{}']/.."
                                    .format(option.get_desc_text(), option.get_header_text()))
        return swipeToElementVerticalWithCount(self.__needed_view_group, 10, self.driver, OS.ANDROID)
