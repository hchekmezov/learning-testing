from src.mobile.abstract.abstract_page import AbstractPage
from src.mobile.mobileTesting.Carina.enums.sex_radio_buttons import SexRadioButton
import abc


class LoginPageBase(AbstractPage):
    __metaclass__ = abc.ABCMeta

    def __init__(self, driver):
        super().__init__(driver)

    @abc.abstractmethod
    def send_name_and_password(self, name, password):
        return

    @abc.abstractmethod
    def is_name_field_present(self):
        return

    @abc.abstractmethod
    def is_password_field_present(self):
        return

    @abc.abstractmethod
    def is_sex_button_present(self, sex: SexRadioButton):
        return

    @abc.abstractmethod
    def is_privacy_policy_checkbox_present(self):
        return

    @abc.abstractmethod
    def is_sex_button_checked(self, sex: SexRadioButton):
        return

    @abc.abstractmethod
    def is_privacy_policy_checked(self):
        return

    @abc.abstractmethod
    def is_sign_up_button_enabled(self):
        return

    @abc.abstractmethod
    def get_text_in_name_field(self):
        return

    @abc.abstractmethod
    def get_text_in_password_field(self):
        return

    @abc.abstractmethod
    def check_sex_radio_button(self, sex: SexRadioButton):
        return

    @abc.abstractmethod
    def check_privacy_policy(self):
        return

    @abc.abstractmethod
    def click_sign_up_button(self):
        return