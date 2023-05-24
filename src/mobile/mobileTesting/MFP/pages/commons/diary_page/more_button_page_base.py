import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.quick_add_page_base import QuickAddPageBase


class MoreButtonPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_quick_add_button(self) -> QuickAddPageBase:
        return
