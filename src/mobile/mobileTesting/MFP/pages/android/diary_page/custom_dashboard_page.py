from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_dashboard_page_base import CustomDashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_summary_page_base import CustomSummaryPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class CustomDashboardPage(CustomDashboardPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//*[@text='Custom Dashboard']")
        self.__back_button = (AppiumBy.XPATH, "//*[@text='Custom Dashboard']"
                                              "//preceding-sibling::android.widget.ImageButton")
        self.__custom_summary_button = (AppiumBy.ID, "com.myfitnesspal.android:id/rbCustomSummary")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__back_button))

    def click_custom_summary_button(self) -> CustomSummaryPageBase:
        self.driver.find_element(*self.__custom_summary_button).click()
        return init_page_or_uiobject(self.driver, CustomSummaryPageBase)

