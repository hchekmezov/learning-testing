import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.newsfeed_sharing_items import NewsfeedSharingItem


class NewsfeedSharingPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_option_checked(self, option: NewsfeedSharingItem) -> bool:
        return

    @abc.abstractmethod
    def click_back_button(self):
        return

    @abc.abstractmethod
    def check_option(self, option: NewsfeedSharingItem):
        return

    @abc.abstractmethod
    def uncheck_option(self, option: NewsfeedSharingItem):
        return
