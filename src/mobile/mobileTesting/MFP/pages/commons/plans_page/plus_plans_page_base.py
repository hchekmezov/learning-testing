import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plan_details_page_base import PlanDetailsPageBase


class PlusPlansPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_on_plan(self, plan: PlansPageItem) -> PlanDetailsPageBase:
        return
