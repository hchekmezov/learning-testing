import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.about_plan_page_base import AboutPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.join_new_plan_page_base import JoinNewPlanPageBase


class PlanDetailsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_needed_plan_opened(self, plan: PlansPageItem) -> bool:
        return

    @abc.abstractmethod
    def click_start_button_zero_plans(self) -> AboutPlanPageBase:
        return

    @abc.abstractmethod
    def click_start_button_one_plan(self) -> JoinNewPlanPageBase:
        return
