import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.plans_page.end_plan_options import EndPlanOption


class EndPlanPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def check_end_option(self, option: EndPlanOption):
        return

    @abc.abstractmethod
    def uncheck_end_option(self, option: EndPlanOption):
        return

    @abc.abstractmethod
    def is_end_option_checked(self, option: EndPlanOption) -> bool:
        return

    @abc.abstractmethod
    def click_end_button(self):
        return
