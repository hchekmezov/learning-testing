from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.preview_page_base import PreviewPageBase
from src.mobile.utils.constants import Constants


class PreviewPage(PreviewPageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.__logo = (AppiumBy.ID, "com.myfitnesspal.android:id/imageLogo")
        self.__login_button = (AppiumBy.ID, "com.myfitnesspal.android:id/buttonLogIn")

    def click_login_button(self):
        self.driver.find_element(self.__login_button[0], self.__login_button[1]).click()

    def is_page_opened(self) -> bool:
        self.wait = WebDriverWait(self.driver, Constants.TEN_SECONDS.value)
        return self.wait.until(EC.visibility_of_element_located(self.__logo)) \
            and self.driver.find_element(self.__login_button[0], self.__login_button[1]).is_displayed()