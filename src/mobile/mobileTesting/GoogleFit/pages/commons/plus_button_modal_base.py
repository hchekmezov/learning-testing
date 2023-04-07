import abc
from selenium.webdriver import Remote

from src.mobile.abstract.abstract_ui_object import AbstractUIObject


class PlusButtonModalBase(AbstractUIObject):
    def __init__(self, driver: Remote):
        super().__init__(driver)


    @abc.abstractmethod
    def is_plus_button_static_on_page(self, locator, container):
        return

    @abc.abstractmethod
    def is_plus_button_below_container_on_page(self, container):
        return

