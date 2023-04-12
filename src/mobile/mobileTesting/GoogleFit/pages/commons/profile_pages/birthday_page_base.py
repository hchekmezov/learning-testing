import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.birthday_page.monthes import Month


class BirthdayPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def change_month_day_year(self, month: Month, day: int, year: int):
        return

    @abc.abstractmethod
    def confirm_changes(self):
        return