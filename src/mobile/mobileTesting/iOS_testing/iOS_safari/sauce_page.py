from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.utils.mobile_utils import *


class SaucePage(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__div_element = (AppiumBy.IOS_PREDICATE, "label == 'I am a div'")
        self.__text_comment = (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`label == 'Comments:'`]")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__div_element)) and \
            self.wait.until(EC.visibility_of_element_located(self.__text_comment))

    def verify_element_text(self):
        assert self.wait.until(EC.visibility_of_element_located(self.__div_element)), "div_element is not present!"