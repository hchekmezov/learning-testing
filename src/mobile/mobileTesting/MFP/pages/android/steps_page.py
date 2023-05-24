from appium.webdriver.common.appiumby import AppiumBy

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
import logging


from src.mobile.mobileTesting.MFP.pages.commons.steps_page_base import StepsPageBase
from appium.webdriver import Remote


logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class StepsPage(StepsPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.TextView")
        self.__enable_checkbox = (AppiumBy.ID, "com.myfitnesspal.android:id/enabled")
        self.__progress_bar = (AppiumBy.ID, "com.myfitnesspal.android:id/progress_spinner")

    def is_page_opened(self) -> bool:
        return self.driver.find_element(self.__title[0], self.__title[1]).text == "Steps" \
            and self.driver.find_element(self.__enable_checkbox[0], self.__enable_checkbox[1]).is_displayed()

    def click_enable_checkbox(self):
        self.driver.find_element(self.__enable_checkbox[0], self.__enable_checkbox[1]).click()

    def is_progress_spinner_rounding_present(self):
        return self.driver.find_element(self.__progress_bar[0], self.__progress_bar[1]).is_displayed()
