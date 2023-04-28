import abc

from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.MFP.enums.my_prem_tools_items import MyPremToolsItem
from src.mobile.utils.mobile_utils import *


class MyPremiumToolsPageBase(AbstractPage):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__needed_view_group = None

    @abc.abstractmethod
    def is_option_and_description_displayed(self, option: MyPremToolsItem) -> bool:
        return
