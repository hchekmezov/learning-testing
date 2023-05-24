import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.custom_summary_item import CustomSummaryItem


class CustomSummaryPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def check_nutrient(self, summary_item: CustomSummaryItem):
        return

    @abc.abstractmethod
    def uncheck_nutrient(self, summary_item: CustomSummaryItem):
        return
    @abc.abstractmethod
    def is_nutrient_checked(self, summary_item: CustomSummaryItem) -> bool:
        return

    @abc.abstractmethod
    def is_save_button_active(self) -> bool:
        return

    @abc.abstractmethod
    def get_nutrient_selected_text(self) -> str:
        return
