import pytest
import logging
import time

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.GoogleFit.pages.android.about_you_page import AboutYouPage
from src.mobile.mobileTesting.GoogleFit.pages.android.continue_as_page import ContinueAsPage
from src.mobile.mobileTesting.GoogleFit.pages.android.home_page import HomePage
from src.mobile.mobileTesting.GoogleFit.pages.android.track_activities_page import TrackActivitiesPage

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def login_method(mobile_driver_opening_and_closing):
    # logger.info("Google fit first test starting...")
    driver = mobile_driver_opening_and_closing
    continue_as_page = ContinueAsPage(driver)
    assert continue_as_page.is_page_opened(), "[Continue As Page] Continue As Page in not opened!"
    continue_as_page.click_continue_as_button()
    about_you_page = AboutYouPage(driver)
    assert about_you_page.is_page_opened(), "[About You Page] About You Page is not " \
                                            "opened after clicking Continue As Button!"
    about_you_page.click_next_button()
    track_activities_page = TrackActivitiesPage(driver)
    assert track_activities_page.is_page_opened(), "[Track Activities Page] Track Activities Page is not " \
                                                   "opened after clicking Next Button!"
    track_activities_page.click_no_thanks_button()
    home_page = HomePage(driver)
    assert home_page.is_page_opened(), "[Home Page] Home Page is not opened after clicking No Thanks Button!"
    return home_page


# check by the XPATH
def test_plus_button_static(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    home_page = login_method(driver)
    assert home_page.is_plus_button_present(), "[Home Page] Plus Button is not present!"
    assert home_page.is_plus_button_static(), "[Home Page] Plus Button is not static!"
    assert home_page.is_plus_button_below_container(), "[Home Page] Plus Button is not below the container!"
