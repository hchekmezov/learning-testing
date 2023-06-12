from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.API_Demos.enums.visibility_page_fields import VisibilityPageField
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.views_page.visibility_page_base import \
    VisibilityPageBase
from src.mobile.utils.mobile_utils import EC


class VisibilityPage(VisibilityPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__visible_button = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/vis")
        self.__invisible_button = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/invis")
        self.__gone_button = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/gone")
        self.__b_field = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/victim")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__visible_button)) and \
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__invisible_button))

    def is_field_visible(self, field: VisibilityPageField):
        try:
            self.driver.find_element(AppiumBy.XPATH, "//*[@text='View {}']".format(field.value))
            return True
        except NoSuchElementException:
            return False

    def click_visible_button(self):
        self.driver.find_element(*self.__visible_button).click()

    def click_invisible_button(self):
        self.driver.find_element(*self.__invisible_button).click()

    def click_gone_button(self):
        self.driver.find_element(*self.__gone_button).click()

