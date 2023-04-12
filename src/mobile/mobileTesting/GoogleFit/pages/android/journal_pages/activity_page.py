from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.commons.journal_pages.activity_page_base import ActivityPageBase
from selenium.webdriver.support import expected_conditions as EC


class ActivityPage(ActivityPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/title")
        self.__more_options_button = (AppiumBy.ACCESSIBILITY_ID, "More options")
        self.__delete_button = (AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/title' "
                                                "and @text='Delete']")
        self.__confirmation_delete_button = (AppiumBy.ID, "android:id/button1")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.wait.until(EC.visibility_of_element_located(self.__more_options_button))

    def delete_activity(self):
        self.driver.find_element(*self.__more_options_button).click()
        self.driver.find_element(*self.__delete_button).click()
        self.driver.find_element(*self.__confirmation_delete_button).click()



