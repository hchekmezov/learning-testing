from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.dashboard_page.goals_options import GoalsOption
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.sure_page_base import SurePageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.goals_page_base import GoalsPageBase


class GoalsPage(GoalsPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                        "/android.widget.TextView[@text='Goals']")
        self.__back_button = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/toolbar']"
                                              "/android.widget.ImageButton")
        self.__needed_option = None

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def click_option(self, option: GoalsOption):
        self.__needed_option = (AppiumBy.XPATH, "//android.widget.TextView[@text='{}']"
                                                "/../../following-sibling::android.widget.LinearLayout"
                                .format(option.value))
        self.driver.find_element(*self.__needed_option).click()
        # return init_page_or_uiobject(self.driver, SurePageBase)

    def click_back_button(self):
        self.driver.find_element(*self.__back_button).click()
