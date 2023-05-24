from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.plans_page.end_plan_options import EndPlanOption
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.end_plan_page_base import EndPlanPageBase
from src.mobile.utils.mobile_utils import EC, logger


class EndPlanPage(EndPlanPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@text='End Plan']")
        self.__end_button = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/endPlan")
        self.__check_box = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__end_button))

    def check_end_option(self, option: EndPlanOption):
        if self.is_end_option_checked(option):
            logger.info("Option <<{}>> already checked! Not need to check it!".format(option.value))
        else:
            self.driver.find_element(*self.__check_box).click()

    def uncheck_end_option(self, option: EndPlanOption):
        if not self.is_end_option_checked(option):
            logger.info("Option <<{}>> already unchecked! Not need to uncheck it!".format(option.value))
        else:
            self.driver.find_element(*self.__check_box).click()

    def is_end_option_checked(self, option: EndPlanOption) -> bool:
        self.__check_box = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android.plans:id/checkBox' "
                                            "and @text='{}']".format(option.value))
        elem = self.driver.find_element(*self.__check_box)
        return False if elem.get_attribute("checked") == 'false' else True

    def click_end_button(self):
        self.driver.find_element(*self.__end_button).click()
