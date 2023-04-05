from src.mobile.mobileTesting.Carina.pages.commons.welcome_page_base import WelcomePageBase
from appium.webdriver.common.mobileby import MobileBy


class WelcomePage(WelcomePageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.__carina_logo = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/carina_logo")
        self.__next_button = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/next_button")

    def is_page_opened(self):
        return self.__carina_logo.is_displayed() and self.__next_button.is_displayed()

    def click_next_button(self):
        self.__next_button.click()


