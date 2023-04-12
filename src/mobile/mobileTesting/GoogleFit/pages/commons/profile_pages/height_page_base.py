import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.height_page.height_measures import HeightMeasure


class HeightPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def change_height(self, left_needed: int, measure: HeightMeasure, right_needed=0):
        return
