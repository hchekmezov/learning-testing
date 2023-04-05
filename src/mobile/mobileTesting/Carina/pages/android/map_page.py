from src.mobile.mobileTesting.Carina.pages.commons.map_page_base import MapPageBase
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC


class MapPage(MapPageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='Map']")))
        self.__title = self.driver.find_element(MobileBy.XPATH, "//android.widget.TextView[@text='Map']")
        self.__navigate_up = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Navigate up")
        self.__zoom_in = self.driver.find_element(MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Zoom in']")
        self.__zoom_out = self.driver.find_element(MobileBy.XPATH, "//android.widget.ImageView[@content-desc='Zoom out']"
                                                                   "/preceding-sibling::android.widget.ImageView[@content-desc='Zoom in']")

    def is_page_opened(self):
        return self.__zoom_in.is_displayed() and self.__zoom_out.is_displayed()

    def click_navigate_up_button(self):
        self.__navigate_up.click()





