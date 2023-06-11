from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.API_Demos.pages.commons.content_page_base import ContentPageBase
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.start_page_base import StartPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class ContentPage(ContentPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__content = (AppiumBy.ID, "android:id/content")
        self.__ok_button = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/buttonDefaultPositive")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__content)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__ok_button))

    def click_ok_button(self) -> StartPageBase:
        self.driver.find_element(*self.__ok_button).click()
        return init_page_or_uiobject(self.driver, StartPageBase)




