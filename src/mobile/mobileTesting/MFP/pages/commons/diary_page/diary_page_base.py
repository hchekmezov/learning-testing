from appium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage

import abc

from src.mobile.mobileTesting.MFP.enums.diary_activity_items import DiaryActivityItem
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_dashboard_page_base import CustomDashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.more_button_page_base import MoreButtonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.nutrition_page_base import NutritionPageBase


class DiaryPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def open_nutrition_page(self) -> NutritionPageBase:
        return

    @abc.abstractmethod
    def click_add_button_on_activity(self, item: DiaryActivityItem):
        return

    @abc.abstractmethod
    def click_more_button_on_activity(self, item: DiaryActivityItem) -> MoreButtonPageBase:
        return

    @abc.abstractmethod
    def is_meal_added(self) -> bool:
        return

    @abc.abstractmethod
    def delete_all_added_meals_in_activity(self, item: DiaryActivityItem):
        return

    @abc.abstractmethod
    def is_all_meals_deleted_in_activity(self, item: DiaryActivityItem) -> bool:
        return

    @abc.abstractmethod
    def is_calories_remaining_chosen(self) -> bool:
        return

    @abc.abstractmethod
    def get_calories_goal_int_value(self) -> int:
        return

    @abc.abstractmethod
    def get_calories_remaining_int_value(self) -> int:
        return

    @abc.abstractmethod
    def clear_user_diary(self):
        return

    @abc.abstractmethod
    def click_summary_more_button(self) -> CustomDashboardPageBase:
        return

