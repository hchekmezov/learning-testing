from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.about_plan_page_base import AboutPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.join_new_plan_page_base import JoinNewPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plan_details_page_base import PlanDetailsPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class PlanDetailsPage(PlanDetailsPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.widget.TextView[@text='Plan Details']")
        self.__button_start = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/btnStartPlan")
        self.__plan_name = (AppiumBy.ID, "com.myfitnesspal.android.plans:id/toolbarTitle")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__button_start))

    def is_needed_plan_opened(self, plan: PlansPageItem) -> bool:
        return self.driver.find_element(*self.__plan_name).text == plan.value[0]

    def click_start_button_zero_plans(self) -> AboutPlanPageBase:
        self.driver.find_element(*self.__button_start).click()
        return init_page_or_uiobject(self.driver, AboutPlanPageBase)

    def click_start_button_one_plan(self) -> JoinNewPlanPageBase:
        self.driver.find_element(*self.__button_start).click()
        return init_page_or_uiobject(self.driver, JoinNewPlanPageBase)
