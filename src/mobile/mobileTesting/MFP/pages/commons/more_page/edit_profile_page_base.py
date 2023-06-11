import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.more_page.edit_profile_options import EditProfileOption
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.sure_page_base import SurePageBase


class EditProfilePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_option(self, option: EditProfileOption):
        return

    @abc.abstractmethod
    def click_back_button(self):
        return