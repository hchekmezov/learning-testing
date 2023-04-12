from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_pages.add_activity_pages.activity_type_page_base import \
    ActivityTypePageBase
from src.mobile.utils.mobile_utils import *
from selenium.webdriver.support import expected_conditions as EC


class ActivityTypePage(ActivityTypePageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/alertTitle")
        self.__random_activity = None
        self.__listview = (AppiumBy.ID, "com.google.android.apps.fitness:id/select_dialog_listview")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title))

    def select_random_activity(self, activity):
        self.__random_activity =(
            AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/select_dialog_listview']"
                            "//*[@text='{}']".format(activity))

        logger.info("Random activity is {}".format(activity))

        if swipe(self.__random_activity,
              self.driver.find_element(*self.__listview),
              Direction.DOWN,
              50,
              200,
              self.driver,
              OS.ANDROID):
            self.driver.find_element(*self.__random_activity).click()




