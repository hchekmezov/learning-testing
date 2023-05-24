import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.plans_page.filter_by_buttons import FilterByButton
from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.end_plan_page_base import EndPlanPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.log_workout_page_base import LogWorkoutPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plan_details_page_base import PlanDetailsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plus_plans_page_base import PlusPlansPageBase


class PlansPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def get_all_filterby_buttons(self):
        return

    @abc.abstractmethod
    def get_all_texts_on_page(self):
        return

    @abc.abstractmethod
    def click_filterby_button(self, button: FilterByButton):
        return

    @abc.abstractmethod
    def click_on_plan(self, plan: PlansPageItem) -> PlanDetailsPageBase:
        return

    @abc.abstractmethod
    def click_plus_button(self) -> PlusPlansPageBase:
        return

    @abc.abstractmethod
    def open_end_plan_page(self) -> EndPlanPageBase:
        return

    @abc.abstractmethod
    def is_text_filter_by_present(self) -> bool:
        return

    @abc.abstractmethod
    def is_all_filter_by_buttons_present(self) -> bool:
        return

    @abc.abstractmethod
    def is_all_texts_and_survey_link_present(self) -> bool:
        return

    @abc.abstractmethod
    def is_plan_shows(self, plan: PlansPageItem) -> bool:
        return

    @abc.abstractmethod
    def is_workout_logged_confirmation_message_present(self) -> bool:
        return

    @abc.abstractmethod
    def check_filter_work_as_expected(self, button: FilterByButton) -> bool:
        return

    @abc.abstractmethod
    def click_log_workout_button(self) -> LogWorkoutPageBase:
        return

    @abc.abstractmethod
    def click_view_button(self) -> DiaryPageBase:
        return
