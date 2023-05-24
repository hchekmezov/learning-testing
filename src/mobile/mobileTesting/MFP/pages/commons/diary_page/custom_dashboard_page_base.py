import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.custom_summary_page_base import CustomSummaryPageBase


class CustomDashboardPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_custom_summary_button(self) -> CustomSummaryPageBase:
        return
