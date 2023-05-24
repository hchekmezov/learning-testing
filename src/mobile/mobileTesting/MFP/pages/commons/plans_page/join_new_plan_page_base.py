import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.about_plan_page_base import AboutPlanPageBase


class JoinNewPlanPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_user_can_add_two_plans(self) -> bool:
        return

    @abc.abstractmethod
    def click_continue_button(self) -> AboutPlanPageBase:
        return
