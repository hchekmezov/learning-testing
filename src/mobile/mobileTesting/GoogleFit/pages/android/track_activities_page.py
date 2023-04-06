from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.commons.track_activities_page_base import TrackActivitiesPageBase
from selenium.webdriver.support import expected_conditions as EC


class TrackActivitiesPage(TrackActivitiesPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__option_description = (AppiumBy.ID, "com.google.android.apps.fitness:id/optin_description")
        self.__no_thanks_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/skip_button")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__option_description)) \
            and self.wait.until(EC.visibility_of_element_located(self.__no_thanks_button))

    def click_no_thanks_button(self):
        self.driver.find_element(self.__no_thanks_button[0], self.__no_thanks_button[1]).click()

