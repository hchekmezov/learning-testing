from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from appium.webdriver import Remote

from src.mobile.mobileTesting.MFP.pages.commons.login_page_base import LoginPageBase
from src.mobile.mobileTesting.MFP.pages.commons.preview_page_base import PreviewPageBase
from src.mobile.utils.constants import Constants
from src.mobile.utils.initialize_utils import init_page_or_uiobject


class PreviewPage(PreviewPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__logo = (AppiumBy.ID, "com.myfitnesspal.android:id/imageLogo")
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/buttonLogIn")

    def click_login_button(self) -> LoginPageBase:
        self.driver.find_element(*self.__login_button).click()
        return init_page_or_uiobject(self.driver, LoginPageBase)

    def is_page_opened(self) -> bool:
        self.wait = WebDriverWait(self.driver, Constants.TEN_SECONDS.value)
        return self.wait.until(EC.visibility_of_element_located(self.__logo)) \
            and self.driver.find_element(*self.__login_button).is_displayed()