from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.commons.about_you_page_base import AboutYouPageBase
from selenium.webdriver.support import expected_conditions as EC


class AboutYouPage(AboutYouPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__next_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/next_button")
        self.__heart_logo = (AppiumBy.ID, "com.google.android.apps.fitness:id/heart_logo_animation")

    def click_next_button(self):
        self.driver.find_element(self.__next_button[0], self.__next_button[1]).click()

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__next_button)) \
               and self.wait.until(EC.visibility_of_element_located(self.__heart_logo))