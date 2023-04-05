import pytest
import logging
import time

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.pages.android.dashbboard_page import DashboardPage
from src.mobile.mobileTesting.MFP.pages.android.existing_user_tutor_page import ExistingUserTutorPage
from src.mobile.mobileTesting.MFP.pages.android.login_page import LoginPage
from src.mobile.mobileTesting.MFP.pages.android.mfp_common_page import MFPCommonPage
from src.mobile.mobileTesting.MFP.pages.android.preview_page import PreviewPage
from jproperties import Properties
import resources
from src.mobile.mobileTesting.MFP.pages.android.steps_page import StepsPage
from src.mobile.utils.constants import Constants
from src.mobile.utils.direction import Direction

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


# configs = Properties()

# with open("_testdata.properties", 'rb') as config_file:
#     configs.load(config_file)

@pytest.mark.skip
def test_mfp_first(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page = MFPCommonPage(driver)
    preview_page = PreviewPage(driver)
    assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    preview_page.click_login_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    # login_page.type_email_and_password(configs.get("email").data, configs.get("password").data)
    login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    login_page.click_login_button()
    assert mfp_common_page.wait_until_spinner_rounding(), \
        "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
    existing_user_tutor_page = ExistingUserTutorPage(driver)
    assert existing_user_tutor_page.is_page_opened(), \
        "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
    existing_user_tutor_page.click_close_button()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    # mfp_common_page.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)


def test_mfp_second(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page = MFPCommonPage(driver)
    preview_page = PreviewPage(driver)
    assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    preview_page.click_login_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    # login_page.type_email_and_password(configs.get("email").data, configs.get("password").data)
    login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    login_page.click_login_button()
    assert mfp_common_page.wait_until_spinner_rounding(), \
        "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
    existing_user_tutor_page = ExistingUserTutorPage(driver)
    assert existing_user_tutor_page.is_page_opened(), \
        "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
    existing_user_tutor_page.click_close_button()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    dashboard_page.click_track_steps_button()
    steps_page = StepsPage(driver)
    assert steps_page.is_page_opened(), "[Steps Page] Steps Page is not opened after clicking Track Steps Button"
    steps_page.click_enable_checkbox()
    assert steps_page.is_progress_spinner_rounding_present()