from src.mobile.mobileTesting.Carina.pages.commons.web_view_page_base import WebViewPageBase
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.utils.mobile_utils import swipeInContainer
from src.mobile.utils.direction import Direction
from src.mobile.utils.operating_system import OS


class WebViewPage(WebViewPageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Web View']")))
        self.__title = (MobileBy.XPATH, "//android.widget.TextView[@text='Web View']")
            # self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Web View']")
        self.__navigate_up = (MobileBy.ACCESSIBILITY_ID, "Navigate up")
            # self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Navigate up")
        self.__image_view = (MobileBy.ID, "com.solvd.carinademoapplication:id/image_view")

    def is_page_opened(self):
        return self.driver.find_element(self.__title[0], self.__title[1]).is_displayed() \
            and self.driver.find_element(self.__navigate_up[0], self.__navigate_up[1]).is_displayed()

    def click_navigate_up_button(self):
        self.driver.find_element(self.__navigate_up[0], self.__navigate_up[1]).click()

    def image_view_swipe_n_times(self, n: int, direction: Direction):
        swipeInContainer(self.driver.find_element(self.__image_view[0], self.__image_view[1]),
                         direction,
                         n,
                         100,
                         self.driver,
                         OS.ANDROID)







