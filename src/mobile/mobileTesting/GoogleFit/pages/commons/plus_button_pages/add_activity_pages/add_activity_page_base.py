import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage



class AddActivityPageBase(AbstractPage):

    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def click_activity_button(self):
        return

    @abc.abstractmethod
    def click_start_date(self):
        return

    @abc.abstractmethod
    def click_start_time(self):
        return

    @abc.abstractmethod
    def click_save_button(self):
        return