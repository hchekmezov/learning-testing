from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plan_details_page_base import PlanDetailsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plus_plans_page_base import PlusPlansPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC, swipeToElementUpWithDuration
from src.mobile.utils.operating_system import OS


class PlusPlansPage(PlusPlansPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title = (AppiumBy.XPATH, "//android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
        self.__active_plans_title = (AppiumBy.XPATH,
                                     "//*[@resource-id='com.myfitnesspal.android.plans:id/plans_segment_header' "
                                     "and @text='Active Plans']")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__active_plans_title))

    def click_on_plan(self, plan: PlansPageItem) -> PlanDetailsPageBase:
        elem = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android.plans:id/plan_name' and @text='{}']"
                .format(plan.value[0]))
        swipeToElementUpWithDuration(elem, 700, self.driver, OS.ANDROID)
        self.driver.find_element(*elem).click()
        return init_page_or_uiobject(self.driver, PlanDetailsPageBase)

