import pytest
import logging

from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.GoogleFit.enums.activities import Activity
from src.mobile.mobileTesting.GoogleFit.enums.home_page_block_title import HomePageBlockTitle
from src.mobile.mobileTesting.GoogleFit.enums.home_page_playlist_title import HomePagePlaylistTitle
from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.enums.plus_button_page_item import PlusButtonPageItem
from src.mobile.mobileTesting.GoogleFit.pages.android.about_you_page import AboutYouPage
from src.mobile.mobileTesting.GoogleFit.pages.android.continue_as_page import ContinueAsPage
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.android.home_page import HomePage
from src.mobile.mobileTesting.GoogleFit.pages.android.journal_pages.activity_page import ActivityPage
from src.mobile.mobileTesting.GoogleFit.pages.android.journal_pages.journal_page import JournalPage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_page import PlusButtonPage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_pages.add_activity_pages.activity_type_page import \
    ActivityTypePage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_pages.add_activity_pages.add_activity_page import AddActivityPage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_pages.add_activity_pages.date_page import DatePage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_pages.add_activity_pages.time_page import TimePage
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
    return home_page


def test_sixth_task_first_point(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    home_page = login_method(driver)
    assert home_page.is_page_opened(), "[Home Page] Home Page is not opened after clicking No Thanks Button!"
    assert home_page.is_plus_button_present(), "[Home Page] Plus Button is not present!"
    assert home_page.is_plus_button_static(), "[Home Page] Plus Button is not static!"
    assert home_page.is_plus_button_below_container(), "[Home Page] Plus Button is not below the container!"

def test_sixth_task_second_point(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    home_page = login_method(driver)
    assert home_page.is_page_opened(), "[Home Page] Home Page is not opened after clicking No Thanks Button!"
    for title in HomePageBlockTitle:
        assert home_page.is_block_by_title_present(title), "[Home Page] Block with title <<{}>> is not present!"\
            .format(title.value)
    titles_from_home_page = home_page.get_list_of_playlist_titles()
    expected_list_of_titles = HomePagePlaylistTitle.get_playlist_titles_values()
    assert set(titles_from_home_page) == set(expected_list_of_titles), "[Home Page] Playlist titles on Home Page " \
                                                                       "are different from Expected List\n" \
                                                                       "Expected: {}\n" \
                                                                       "Actual: {}".format(
                                                                        expected_list_of_titles, titles_from_home_page)

def test_seventh_task_first_point(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    home_page = login_method(driver)
    assert home_page.is_page_opened(), "[Home Page] Home Page is not opened after clicking No Thanks Button!"
    home_page.click_plus_button()
    plus_button_page = PlusButtonPage(driver)
    assert plus_button_page.is_page_opened(), "[Plus Button Page] Plus Button Page is not opened " \
                                              "after clicking Plus Button!"
    plus_button_page.click_item_on_page(PlusButtonPageItem.ADD_ACTIVITY)
    add_activity_page = AddActivityPage(driver)
    assert add_activity_page.is_page_opened(), "[Add Activity Page] Add Activity Page is not opened after clicking " \
                                               "Add activity Button!"
    add_activity_page.click_activity_button()
    activity_type_page = ActivityTypePage(driver)
    assert activity_type_page.is_page_opened(), "[Activity Type Page] Activity Type Page is not opened " \
                                                "after clicking Activity Button!"
    variants = [e.value for e in Activity]
    # activity_type_page.select_random_activity(variants[random.randint(0, len(variants))])
    infos_about_activity = []
    activity_type_page.select_random_activity(variants[len(variants) - 1])

    infos_about_activity.append(variants[len(variants) - 1])

    add_activity_page = AddActivityPage(driver)
    assert add_activity_page.is_page_opened(), "[Add Activity Page] Add Activity Page is not opened after choosing " \
                                               "random activity!"
    add_activity_page.click_start_date()
    date_page = DatePage(driver)
    assert date_page.is_page_opened(), "[Date Page] Date Page is not opened after clicking start date button!"

    infos_about_activity.append(date_page.click_needed_date(4))

    date_page.click_ok_button()
    add_activity_page = AddActivityPage(driver)
    assert add_activity_page.is_page_opened(), "[Add Activity Page] Add Activity Page is not opened after choosing " \
                                               "start date!"
    add_activity_page.click_start_time()
    time_page = TimePage(driver)
    assert time_page.is_page_opened(), "[Time Page] Time Page is not opened after clicking start time button!"

    infos_about_activity.append(time_page.set_hours_and_minutes(12, 25))

    time_page.click_ok_button()
    add_activity_page = AddActivityPage(driver)
    assert add_activity_page.is_page_opened(), "[Add Activity Page] Add Activity Page is not opened after choosing " \
                                               "start time!"
    add_activity_page.click_save_button()
    home_page = HomePage(driver)
    assert home_page.is_page_opened(), "[Home Page] Home Page is not opened after clicking Save button!"

    gf_common_page = GFCommonPage(driver)
    gf_common_page.get_bottom_nav_container().click_nav_container_button(NavContainerButton.JOURNAL)

    journal_page = JournalPage(driver)
    assert journal_page.is_page_opened(), "[Journal Page] Journal Page is not opened!"
    assert journal_page.is_activity_right(infos_about_activity[0], infos_about_activity[2], infos_about_activity[1]), \
        "[Journal Page] Activity is not the same on Journal Page!"
    journal_page.click_activity_view_group()
    activity_page = ActivityPage(driver)
    assert activity_page.is_page_opened(), "[Activity Page] Activity Page is not opened after clicking " \
                                           "Activity View Group!"
    activity_page.delete_activity()
    journal_page = JournalPage(driver)
    assert journal_page.is_page_opened(), "[Journal Page] Journal Page is not opened after deleting activity!"










