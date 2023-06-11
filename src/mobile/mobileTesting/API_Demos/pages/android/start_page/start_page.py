
from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.enums.start_page_items import StartPageItem
from src.mobile.utils.initialize_utils import init_page_or_uiobject

from src.mobile.utils.mobile_utils import EC
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.start_page_base import StartPageBase


class StartPage(StartPageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title_container = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/shimmer_view_container")
        self.__search_button = (AppiumBy.ACCESSIBILITY_ID, "Search")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title_container)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__search_button))

    def open_page(self, item: StartPageItem) -> AbstractPage:
        self.driver.find_element(AppiumBy.XPATH, item.get_xpath()).click()
        return init_page_or_uiobject(self.driver, item.get_base_class())

