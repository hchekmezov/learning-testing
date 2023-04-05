from src.mobile.abstract.abstract_page import AbstractPage
import abc

class UIElementsPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver):
        super().__init__(driver)

    @abc.abstractmethod
    def click_navigate_up_button(self):
        return

    @abc.abstractmethod
    def is_enable_switch_present(self):
        return

    # @abc.abstractmethod
    # def find_by_swiping(self):
    #     return