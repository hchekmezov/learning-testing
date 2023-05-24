from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.plans_page.about_plan_page_base import AboutPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.join_new_plan_page_base import JoinNewPlanPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC

class JoinNewPlanPage(JoinNewPlanPageBase):

    MESSAGE = 'If you join this new plan, your current active plan will end. Do you want to continue?'

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__message = (AppiumBy.ID, "com.myfitnesspal.android:id/message")
        self.__continue_button = (AppiumBy.ID, "com.myfitnesspal.android:id/positiveBtn")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__message)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__continue_button))

    def is_user_can_add_two_plans(self) -> bool:
        return self.driver.find_element(*self.__message).text != self.MESSAGE

    def click_continue_button(self) -> AboutPlanPageBase:
        self.driver.find_element(*self.__continue_button).click()
        return init_page_or_uiobject(self.driver, AboutPlanPageBase)
