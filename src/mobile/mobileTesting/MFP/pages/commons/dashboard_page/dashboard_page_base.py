import abc

from appium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase


class DashboardPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_track_steps_button(self):
        return

    @abc.abstractmethod
    def click_user_avatar(self) -> UserPageBase:
        return
