import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.home_page.home_page_block_title import HomePageBlockTitle
from src.mobile.mobileTesting.GoogleFit.enums.home_page.home_page_first_titles import FirstTitles


class HomePageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def get_plus_button(self):
        return

    @abc.abstractmethod
    def is_plus_button_static(self):
        return

    @abc.abstractmethod
    def is_plus_button_present(self):
        return

    @abc.abstractmethod
    def is_plus_button_below_container(self):
        return

    @abc.abstractmethod
    def is_block_by_title_present(self, title: HomePageBlockTitle):
        return

    @abc.abstractmethod
    def get_list_of_playlist_titles(self):
        return

    @abc.abstractmethod
    def click_plus_button(self):
        return

    @abc.abstractmethod
    def get_color_of_account_image(self):
        return




