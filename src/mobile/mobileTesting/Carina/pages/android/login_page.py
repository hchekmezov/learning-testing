from src.mobile.mobileTesting.Carina.enums.sex_radio_buttons import SexRadioButton
from src.mobile.mobileTesting.Carina.pages.commons.login_page_base import LoginPageBase
from appium.webdriver.common.mobileby import MobileBy
import logging
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class LoginPage(LoginPageBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait.until(EC.presence_of_element_located((MobileBy.ID, "com.solvd.carinademoapplication:id/backButton")))
        self.__back_button = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/backButton")
        self.__sign_up_button = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/login_button")
        self.__name_field = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/name")
        self.__password_field = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/password")
        self.__privacy_policy_checkbox = self.driver.find_element(MobileBy.ID, "com.solvd.carinademoapplication:id/checkbox")

    def is_page_opened(self):
        return self.__back_button.is_displayed() and self.__sign_up_button.is_displayed()

    def send_name_and_password(self, name, password):
        self.__name_field.send_keys(name)
        self.__password_field.send_keys(password)

    def is_name_field_present(self):
        return self.__name_field.is_displayed()

    def is_password_field_present(self):
        return self.__password_field.is_displayed()

    def is_sex_button_present(self, sex: SexRadioButton):
        return self.driver.find_element(MobileBy.ID, f"com.solvd.carinademoapplication:id/radio_{sex.value.lower()}").is_displayed()

    def is_privacy_policy_checkbox_present(self):
        return self.__privacy_policy_checkbox.is_displayed()

    def is_sex_button_checked(self, sex: SexRadioButton):
        if self.driver.find_element(MobileBy.ID, f"com.solvd.carinademoapplication:id/radio_{sex.value.lower()}")\
                .get_attribute('checked') == 'true':
            return True
        else:
            return False

    def is_privacy_policy_checked(self):
        if self.__privacy_policy_checkbox.get_attribute('checked') == 'true':
            return True
        else:
            return False

    def is_sign_up_button_enabled(self):
        return self.__sign_up_button.is_enabled()

    def get_text_in_name_field(self):
        return self.__name_field.text

    def get_text_in_password_field(self):
        return self.__password_field.text

    def check_sex_radio_button(self, sex: SexRadioButton):
        self.driver.find_element(MobileBy.ID, f"com.solvd.carinademoapplication:id/radio_{sex.value.lower()}").click()

    def check_privacy_policy(self):
        self.__privacy_policy_checkbox.click()

    def click_sign_up_button(self):
        self.__sign_up_button.click()








