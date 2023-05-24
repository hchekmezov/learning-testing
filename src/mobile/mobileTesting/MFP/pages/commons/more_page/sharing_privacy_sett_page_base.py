import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.sharing_privacy_items import SharingPrivacyItem


class SharingPrivacySettingsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_sharing_privacy_option(self, option: SharingPrivacyItem) -> AbstractPage:
        return

    @abc.abstractmethod
    def click_back_button(self):
        return
