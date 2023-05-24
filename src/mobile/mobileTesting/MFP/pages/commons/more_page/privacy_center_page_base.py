import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.privacy_center_items import PrivacyCenterItem


class PrivacyCenterPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_privacy_center_option(self, option: PrivacyCenterItem) -> AbstractPage:
        return

    @abc.abstractmethod
    def click_back_button(self):
        return
