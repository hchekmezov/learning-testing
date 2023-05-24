from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.more_button_page_base import MoreButtonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.quick_add_page_base import QuickAddPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class MoreButtonPage(MoreButtonPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__quick_add_button = (AppiumBy.XPATH, "//*[@text='Quick Add']/..")
        self.__reminders_button = (AppiumBy.XPATH, "//*[@text='Reminders']/..")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__reminders_button)) \
            and WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__quick_add_button))

    def click_quick_add_button(self) -> QuickAddPageBase:
        self.driver.find_element(*self.__quick_add_button).click()
        return init_page_or_uiobject(self.driver, QuickAddPageBase)

