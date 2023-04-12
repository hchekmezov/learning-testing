from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import Remote

import logging
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.GoogleFit.pages.commons.plus_button_pages.add_activity_pages.date_page_base import \
    DatePageBase
from selenium.webdriver.support import expected_conditions as EC


logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)

class DatePage(DatePageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__picker_header = (AppiumBy.ID, "com.google.android.apps.fitness:id/mtrl_picker_header")
        self.__needed_day = None
        self.__ok_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/confirm_button")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__picker_header)) \
            and self.wait.until(EC.visibility_of_element_located(self.__ok_button))

    def click_needed_date(self, index: int):
        self.__needed_day = (AppiumBy.XPATH, "(//*[@resource-id='com.google.android.apps.fitness:id/month_grid']"
                                             "/android.widget.TextView)[{}]".format(index))
        element = self.driver.find_element(*self.__needed_day)
        element.click()
        tmp = element.get_attribute("content-desc")
        if "Today " in tmp:
            tmp = tmp[6:]
        return tmp

    def click_ok_button(self):
        self.driver.find_element(*self.__ok_button).click()




