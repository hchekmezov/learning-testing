import abc

from appium.webdriver import Remote

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.add_nutrient_info_page_base import \
    AddNutrientInfoPageBase


class CreateFoodPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def fill_all_fields_by_default_values(self)  -> AddNutrientInfoPageBase:
        return
