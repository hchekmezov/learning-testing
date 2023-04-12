import abc

from selenium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.GoogleFit.enums.profile_page.weight_page.weight_measures import WeightMeasure


class WeightPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def change_weight(self, left_needed: int, right_needed: int, measure: WeightMeasure):
        return