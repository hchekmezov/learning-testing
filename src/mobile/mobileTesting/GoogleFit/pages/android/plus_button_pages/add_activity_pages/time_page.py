from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote, Keys

import logging
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_pages.add_activity_pages.time_page_base import \
    TimePageBase

from selenium.webdriver.support import expected_conditions as EC



logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

class TimePage(TimePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.ID, "com.google.android.apps.fitness:id/header_title")
        self.__hours = None
        self.__minutes = None
        self.__ok_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/material_timepicker_ok_button")
        self.__clock_mode_button = (AppiumBy.ACCESSIBILITY_ID, "Switch to clock mode for the time input.")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__title)) \
            and self.wait.until(EC.visibility_of_element_located(self.__ok_button))

    def set_hours_and_minutes(self, hours: int, minutes: int):
        self.driver.find_element(*self.__clock_mode_button).click()
        hours_str = str(hours)
        if hours == 0:
            self.__hours = (
                AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/material_clock_face']"
                                "/android.widget.TextView[@content-desc='00 hours']")
            hours_str = '00'
        else:
            self.__hours = (
                AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/material_clock_face']"
                                "/android.widget.TextView[@content-desc='{} hours']".format(hours))
            hours_str = str(hours)

        self.driver.find_element(*self.__hours).click()
        minutes_str = str(minutes)
        if minutes % 5 == 0:
            if minutes < 10 and minutes >= 0:
                self.__minutes = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='0{} minutes']".format(minutes))
                minutes_str = '0' + str(minutes)
            else:
                self.__minutes = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc='{} minutes']".format(minutes))
                minutes_str = str(minutes)
        else:
            raise Exception('Wrong number for minutes! Minutes should be like minutes % 5 == 0!')

        self.driver.find_element(*self.__minutes).click()
        # self.driver.find_element(*self.__ok_button).click()
        self.driver.hide_keyboard()
        s_res = hours_str + ":" + minutes_str
        return s_res

    # def send_keys_to_hours(self, hours: int):
    #     if hours > 24 or hours < 0:
    #         raise Exception('Wrong number for hours!')
    #
    #     try:
    #         web_element = self.driver.find_element(*self.__hours_view)
    #         web_element.click()
    #     except NoSuchElementException:
    #         logger.info('No need to find element {}'.format(self.__hours_view))
    #     finally:
    #         self.__hours = (
    #             AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/material_hour_text_input']"
    #                         "//android.widget.EditText"
    #             )
    #         self.driver.find_element(*self.__hours).send_keys(hours)
    #
    # def send_keys_to_minutes(self, minutes: int):
    #     if minutes > 60 or minutes < 0:
    #         raise Exception('Wrong number for minutes!')
    #
    #     try:
    #         web_element = self.driver.find_element(*self.__minutes_view)
    #         web_element.click()
    #     except NoSuchElementException:
    #         logger.info('No need to find element {}'.format(self.__minutes_view))
    #     finally:
    #         self.__minutes = (
    #             AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/material_minute_text_input']"
    #                         "//android.widget.EditText"
    #             )
    #         self.driver.find_element(*self.__minutes).send_keys(minutes)


    def click_ok_button(self):
        self.driver.find_element(*self.__ok_button).click()






