from src.mobile.mobileTesting.Carina.pages.commons.ui_elements_page_base import UIElementsPageBase
from appium.webdriver.common.mobileby import MobileBy
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.direction import Direction
from src.mobile.utils.operating_system import OS
from selenium.webdriver.support import expected_conditions as EC



class UIElementsPage(UIElementsPageBase):


    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH, "//android.widget.TextView[@text='UI elements']")))
        self.driver = driver
        self.__title = (MobileBy.XPATH, "//android.widget.TextView[@text='UI elements']")
        self.__navigate_up = (MobileBy.ACCESSIBILITY_ID, "Navigate up")
        self.__imageView = (MobileBy.ID, "com.solvd.carinademoapplication:id/imageView")
        self.__textField = (MobileBy.ID, "com.solvd.carinademoapplication:id/editText")
        self.__emailField = (MobileBy.ID, "com.solvd.carinademoapplication:id/editText2")
        self.__dateField = (MobileBy.ID, "com.solvd.carinademoapplication:id/editText3")
        self.__copyCheckbox = (MobileBy.ID, "com.solvd.carinademoapplication:id/checkBox2")
        self.__enable = (MobileBy.ID, "com.solvd.carinademoapplication:id/switch1")
        self.__container = (MobileBy.XPATH, "//android.widget.ScrollView/android.view.ViewGroup")

    def is_page_opened(self):
        return self.driver.find_element(self.__title[0], self.__title[1]).is_displayed() \
            and self.driver.find_element(self.__copyCheckbox[0], self.__copyCheckbox[1]).is_displayed()

    def click_navigate_up_button(self):
        self.driver.find_element(self.__navigate_up[0], self.__navigate_up[1]).click()

    def is_enable_switch_present(self):
        # return swipe(locator=self.__enable,
        #              container=self.driver.find_element(self.__container[0], self.__container[1]),
        #              direction=Direction.UP,
        #              count=5,
        #              duration=1000,
        #              driver=self.driver,
        #              os=OS.ANDROID)
        return swipeWithDirection(locator=self.__enable,
                                  container=self.driver.find_element(self.__container[0], self.__container[1]),
                                  direction=Direction.VERTICAL,
                                  driver=self.driver,
                                  os=OS.ANDROID)









