from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.existing_user_tutor_page_base import ExistingUserTutorPageBase
from selenium.webdriver.support import expected_conditions as EC

from src.mobile.utils.initialize_utils import init_page_or_uiobject


class ExistingUserTutorPage(ExistingUserTutorPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__close_button = (AppiumBy.XPATH, "//android.view.View [@resource-id='buttonExistingUserTutorial']/android.widget.Button")
        self.__see_tutorial_button = (AppiumBy.XPATH, "//android.view.View[@resource-id='buttonSeeTutorial']")

    def click_close_button(self) -> DashboardPageBase:
        self.driver.find_element(*self.__close_button).click()
        return init_page_or_uiobject(self.driver, DashboardPageBase)


    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.__close_button)) \
            and self.driver.find_element(*self.__see_tutorial_button).is_displayed()