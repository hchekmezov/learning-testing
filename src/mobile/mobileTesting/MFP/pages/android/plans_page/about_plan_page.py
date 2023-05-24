from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.plans_page.about_plan_page_base import AboutPlanPageBase
from src.mobile.utils.mobile_utils import EC

class AboutPlanPage(AboutPlanPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__plan_image = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/planImage")
        self.__continue_button = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/welcomeActionBtn")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__plan_image)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__continue_button))

    def click_continue_button(self):
        self.driver.find_element(*self.__continue_button).click()
