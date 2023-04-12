from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from selenium.webdriver.support import expected_conditions as EC


from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_pages.add_activity_pages.add_activity_page_base import \
    AddActivityPageBase


class AddActivityPage(AddActivityPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/expanded_title")
        self.__close_button = (AppiumBy.ACCESSIBILITY_ID, "Close")
        self.__activity = (AppiumBy.ID, "com.google.android.apps.fitness:id/activity_field")
        self.__start_date = (AppiumBy.ID, "com.google.android.apps.fitness:id/date_button")
        self.__start_time = (AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/date_button']"
                                             "//following-sibling::android.widget.Button")
        self.__duration_time = (AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/duration_field']"
                                                 "//child::android.widget.Button")
        self.__save_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/container_action_button")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.wait.until(EC.visibility_of_element_located(self.__close_button))

    def click_activity_button(self):
        self.driver.find_element(*self.__activity).click()

    def click_start_date(self):
        self.driver.find_element(*self.__start_date).click()

    def click_start_time(self):
        self.driver.find_element(*self.__start_time).click()

    def click_save_button(self):
        self.driver.find_element(*self.__save_button).click()







