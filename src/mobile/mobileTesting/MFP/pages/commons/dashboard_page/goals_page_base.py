import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.dashboard_page.activity_level import ActivityLevel
from src.mobile.mobileTesting.MFP.enums.dashboard_page.goals_options import GoalsOption
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.sure_page_base import SurePageBase


class GoalsPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_option(self, option: GoalsOption):
        return

    @abc.abstractmethod
    def click_back_button(self):
        return