import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.more_menu_options import MoreMenuOption


class MorePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_option_present(self, option: MoreMenuOption) -> bool:
        return

    @abc.abstractmethod
    def click_option(self, option: MoreMenuOption) -> AbstractPage:
        return
