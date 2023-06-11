import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.dashboard_page.weekly_goal_items import WeeklyGoalItem


class WeeklyGoalPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def set_weekly_goal(self, goal: WeeklyGoalItem):
        return