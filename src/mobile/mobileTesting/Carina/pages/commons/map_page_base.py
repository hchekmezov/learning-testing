from src.mobile.abstract.abstract_page import AbstractPage
import abc


class MapPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver):
        super().__init__(driver)

    @abc.abstractmethod
    def click_navigate_up_button(self):
        return



