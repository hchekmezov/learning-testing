from src.mobile.mobileTesting.Carina.pages.commons.navigate_up_menu_base import NavigateUpMenuBase
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as EC
from src.mobile.mobileTesting.Carina.enums.navigate_up_menu_item import NavigateUpMenuItem


class NavigateUpMenuPage(NavigateUpMenuBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(EC.presence_of_element_located((MobileBy.XPATH,
                                                        "//android.widget.LinearLayout[@resource-id='com.solvd.carinademoapplication:id/navigation_header_container']//android.widget.ImageView")))
        self.__photo = self.driver.find_element(MobileBy.XPATH,
                                                "//android.widget.LinearLayout[@resource-id='com.solvd.carinademoapplication:id/navigation_header_container']//android.widget.ImageView")
        self.__top_text = self.driver.find_element(MobileBy.XPATH,
                                                   "(//android.widget.LinearLayout[@resource-id='com.solvd.carinademoapplication:id/navigation_header_container']//android.widget.TextView)[1]")

    def is_page_opened(self):
        return self.__photo.is_displayed() and self.__top_text.is_displayed()

    def click_navigate_up_menu_item(self, nav_up_item: NavigateUpMenuItem):
        self.driver.find_element(MobileBy.XPATH, f"//android.widget.CheckedTextView[@text='{nav_up_item.value}']").click()
