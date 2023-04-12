import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.pages_from_about_you import PageFromAboutYou


class ProfilePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def open_page_from_about_you(self, page: PageFromAboutYou):
        return

    @abc.abstractmethod
    def check_all_changed_info(self, gender, birthday, weight, height) -> bool:
        return