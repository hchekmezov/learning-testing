from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.add_nutrient_info_page_base import \
    AddNutrientInfoPageBase
from src.mobile.utils.mobile_utils import EC


class AddNutrientInfoPage(AddNutrientInfoPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/title_template")
        self.__no_thanks_button = (AppiumBy.ID, "android:id/button2")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__no_thanks_button))

    def click_no_thanks_button(self):
        self.driver.find_element(*self.__no_thanks_button).click()
