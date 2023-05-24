import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.settings_items import SettingsItem


class SettingsPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_settings_page_option(self, option: SettingsItem) -> AbstractPage:
        return

    @abc.abstractmethod
    def click_back_button(self):
        return
