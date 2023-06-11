from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.views_page.drag_and_drop_page_base import \
    DragAndDropPageBase
from src.mobile.utils.mobile_utils import EC, drag_and_drop


class DragAndDropPage(DragAndDropPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__explanation = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/drag_explanation")
        self.__drag_dot_1 = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/drag_dot_1")
        self.__drag_dot_2 = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/drag_dot_2")
        self.__drag_text = (AppiumBy.ID, "com.touchboarder.android.api.demos:id/drag_text")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__drag_dot_2)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__drag_dot_1))

    def make_drag_and_drop_dot1_and_dot2(self):
        drag_and_drop(self.driver,
                      self.driver.find_element(*self.__drag_dot_1),
                      self.driver.find_element(*self.__drag_dot_2))

    def is_drag_and_dropped_dot1_and_dot2(self) -> bool:
        return len(self.driver.find_element(*self.__drag_text).text) != 0



