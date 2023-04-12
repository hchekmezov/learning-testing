from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.commons.journal_pages.journal_page_base import JournalPageBase
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import logging
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler


logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

class JournalPage(JournalPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__toolbar = (AppiumBy.ID, "com.google.android.apps.fitness:id/collapsing_toolbar")
        # self.__swipe_layout = (AppiumBy.ID, "com.google.android.apps.fitness:id/swipe_refresh_layout")
        self.__date_title = None
        self.__start_time = (AppiumBy.ID, "com.google.android.apps.fitness:id/session_start_time")
        self.__activity = None
        self.__activity_view_group = (AppiumBy.XPATH, "//android.support.v7.widget.RecyclerView/android.view.ViewGroup")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__toolbar)) \
            and GFCommonPage(self.driver) \
                .get_bottom_nav_container() \
                .is_nav_container_button_selected(NavContainerButton.JOURNAL)

    def is_activity_right(self, activity: str, time: str, date: str) -> bool:
        self.__activity = (AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='{}']".format(activity))
        try:
            self.driver.find_element(*self.__activity)
        except NoSuchElementException:
            logger.info("Activities aren't the same!")
            return False

        if self.driver.find_element(*self.__start_time).text != time:
            logger.info("Start times aren't the same!")
            return False

        self.__date_title = (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']".format(date))
        try:
            self.driver.find_element(*self.__date_title)
        except NoSuchElementException:
            logger.info(self.__date_title[1])
            logger.info("Dates aren't the same!")
            return False

        return True

    def click_activity_view_group(self):
        self.driver.find_element(*self.__activity_view_group).click()





