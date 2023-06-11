from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.enums.api_demos_page_items import ApiDemosPageItem

from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.api_demos_page_base import ApiDemosPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC

class ApiDemosPage(ApiDemosPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__back_button = (AppiumBy.ACCESSIBILITY_ID, "Navigate up")
        self.__title = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"
                                        "/following-sibling::android.widget.TextView[@text='API Demos']")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title))

    def open_page(self, item: ApiDemosPageItem) -> AbstractPage:
        self.driver.find_element(AppiumBy.XPATH, item.get_xpath()).click()
        return init_page_or_uiobject(self.driver, item.get_base_class())

