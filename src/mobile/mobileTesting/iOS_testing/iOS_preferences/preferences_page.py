from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.utils.mobile_utils import EC


class PreferencesPage(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__general_button = (AppiumBy.IOS_CLASS_CHAIN,
                                 "**/XCUIElementTypeCell[`label == 'General'`]")

    def click_general_button(self):
        self.wait.until(EC.visibility_of_element_located(self.__general_button))
        self.driver.find_element(*self.__general_button).click()