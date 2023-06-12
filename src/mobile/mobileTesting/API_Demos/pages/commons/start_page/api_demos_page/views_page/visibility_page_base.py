import abc

from appium.webdriver import Remote
from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.API_Demos.enums.visibility_page_fields import VisibilityPageField


class VisibilityPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)

    @abc.abstractmethod
    def is_field_visible(self, field: VisibilityPageField):
        return

    @abc.abstractmethod
    def click_visible_button(self):
        return

    @abc.abstractmethod
    def click_invisible_button(self):
        return

    @abc.abstractmethod
    def click_gone_button(self):
        return