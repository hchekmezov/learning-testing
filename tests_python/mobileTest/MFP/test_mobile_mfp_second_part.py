import logging

import pytest
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.common_utils.soft_assert import SoftAssert
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.more_page.more_menu_options import MoreMenuOption
from src.mobile.mobileTesting.MFP.enums.more_page.newsfeed_sharing_items import NewsfeedSharingItem
from src.mobile.mobileTesting.MFP.enums.more_page.privacy_center_items import PrivacyCenterItem
from src.mobile.mobileTesting.MFP.enums.more_page.settings_items import SettingsItem
from src.mobile.mobileTesting.MFP.enums.more_page.sharing_privacy_items import SharingPrivacyItem
from src.mobile.mobileTesting.MFP.enums.plans_page.end_plan_options import EndPlanOption
from src.mobile.mobileTesting.MFP.enums.plans_page.filter_by_buttons import FilterByButton
from src.mobile.mobileTesting.MFP.enums.plans_page.plans_page_items import PlansPageItem
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.more_page_base import MorePageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.privacy_center_page_base import PrivacyCenterPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.settings_page_base import SettingsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.sharing_privacy_sett_page_base import \
    SharingPrivacySettingsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.plans_page.plans_page_base import PlansPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import attach_screenshot
from tests_python.mobileTest.MFP.test_mobile_mfp import login_to_dashboard

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


@pytest.mark.skip
def test_case_nine(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    assert plans_page_base.is_text_filter_by_present(), "[Plans Page] Text Filter by is not present!"
    assert plans_page_base.is_all_filter_by_buttons_present(), "[Plans Page] Not all buttons present!"
    assert plans_page_base.is_all_texts_and_survey_link_present(), "[Plans Page] Not all texts or survey link present!"


@pytest.mark.skip
def test_case_ten(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    members_of_filterby_buttons = FilterByButton.__members__.keys()
    soft_assert = SoftAssert()
    for state in members_of_filterby_buttons:
        soft_assert.assert_expression(plans_page_base.check_filter_work_as_expected(FilterByButton[state]),
                                      "[Plans Page] Wrong texts for {}!".format(FilterByButton[state]))
    soft_assert.assert_all()


@pytest.mark.skip
def test_case_eleven(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    plan_details_page_base = plans_page_base.click_on_plan(PlansPageItem.EAT_GREEN)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.EAT_GREEN)
    attach_screenshot(driver)

    about_plan_page_base = plan_details_page_base.click_start_button_zero_plans()
    assert about_plan_page_base.is_page_opened(), "[About Plan Page] About Plan Page is not opened " \
                                                  "after choosing and start plan!"
    attach_screenshot(driver)

    about_plan_page_base.click_continue_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking Continue Button!"
    assert plans_page_base.is_plan_shows(PlansPageItem.EAT_GREEN), "[Plans Page] Not found needed title for plan! " \
                                                                   "Should be {}"\
                                                                    .format(PlansPageItem.EAT_GREEN.value[0])
    attach_screenshot(driver)

    plus_plans_page_base = plans_page_base.click_plus_button()
    assert plus_plans_page_base.is_page_opened(), "[Plus Plans Page] Plus Plans Page is not " \
                                                  "opened after clicking Plus Button!"
    attach_screenshot(driver)

    plan_details_page_base = plus_plans_page_base.click_on_plan(PlansPageItem.PROGRESSIVE_DUMBBELL)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.PROGRESSIVE_DUMBBELL)
    attach_screenshot(driver)

    join_new_plan_page_base = plan_details_page_base.click_start_button_one_plan()
    assert join_new_plan_page_base.is_page_opened(), "[Join New Plan Page] Join New Plan Page is not opened after " \
                                                     "clicking Start plan button!"
    attach_screenshot(driver)
    assert not join_new_plan_page_base.is_user_can_add_two_plans(), \
        '[Join New Plan Page] User can add two active plans!'

    about_plan_page_base = join_new_plan_page_base.click_continue_button()
    assert about_plan_page_base.is_page_opened(), "[About Plan Page] About Plan Page is not opened " \
                                                  "after choosing and start plan!"
    attach_screenshot(driver)

    about_plan_page_base.click_continue_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking Continue Button!"
    assert plans_page_base.is_plan_shows(PlansPageItem.PROGRESSIVE_DUMBBELL), \
        "[Plans Page] Not found needed title for plan! Should be {}" \
        .format(PlansPageItem.PROGRESSIVE_DUMBBELL.value[0])


@pytest.mark.skip
def test_case_twelve(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    user_page_base = dashboard_page_base.click_user_avatar()
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking on User Avatar!"
    attach_screenshot(driver)

    user_page_base.click_my_items_tab()
    food_value_before = user_page_base.get_current_food_count()
    create_food_page_base = user_page_base.click_create_food_button()
    assert create_food_page_base.is_page_opened(), "[Create Food Page] Create Food Page is not opened after " \
                                                   "clicking Create Button!"
    attach_screenshot(driver)

    add_nutrient_info_page_base = create_food_page_base.fill_all_fields_by_default_values()
    assert add_nutrient_info_page_base.is_page_opened(), "[Add Nutrient Page] Add Nutrient Page is not opened!"
    attach_screenshot(driver)

    add_nutrient_info_page_base.click_no_thanks_button()
    user_page_base = init_page_or_uiobject(driver, UserPageBase)
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after adding food!"
    attach_screenshot(driver)

    food_value_after = user_page_base.get_current_food_count()
    assert food_value_after == (food_value_before + 1), "[User Page] Amount of food not properly changed! " \
                                                        "Before adding food: {}, After adding food: {}"\
                                                        .format(food_value_before, food_value_after)

@pytest.mark.skip
def test_case_thirteen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    plan_details_page_base = plans_page_base.click_on_plan(PlansPageItem.EAT_GREEN)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.EAT_GREEN)
    attach_screenshot(driver)

    about_plan_page_base = plan_details_page_base.click_start_button_zero_plans()
    assert about_plan_page_base.is_page_opened(), "[About Plan Page] About Plan Page is not opened " \
                                                  "after choosing and start plan!"
    attach_screenshot(driver)

    about_plan_page_base.click_continue_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking Continue Button!"
    assert plans_page_base.is_plan_shows(PlansPageItem.EAT_GREEN), "[Plans Page] Not found needed title for plan! " \
                                                                   "Should be {}"\
                                                                    .format(PlansPageItem.EAT_GREEN.value[0])
    attach_screenshot(driver)

    end_plan_page_base = plans_page_base.open_end_plan_page()
    assert end_plan_page_base.is_page_opened(), "[End Plan Page] End Plan Page is not opened!"
    attach_screenshot(driver)

    options_to_check = [EndPlanOption.FORGOT, EndPlanOption.WANT_DIFFERENT_PLAN, EndPlanOption.LOST_INTEREST]
    for option in options_to_check:
        end_plan_page_base.check_end_option(option)
    attach_screenshot(driver)

    soft_assert = SoftAssert()
    for option in options_to_check:
        soft_assert.assert_expression(end_plan_page_base.is_end_option_checked(option),
                                "[End Plan Page] Option <<{}>> is not checked while it should be!".format(option.value))

    for option in options_to_check:
        end_plan_page_base.uncheck_end_option(option)
    attach_screenshot(driver)

    for option in options_to_check:
        soft_assert.assert_expression(not end_plan_page_base.is_end_option_checked(option),
                                "[End Plan Page] Option <<{}>> is not checked while it should be!".format(option.value))

    soft_assert.assert_all()

    end_plan_page_base.click_end_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking End Plan Button!"


@pytest.mark.skip
def test_case_fourteen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    newsfeed_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.NEWSFEED)
    assert newsfeed_page_base.is_page_opened(), "[Newsfeed Page] Newsfeed Page is not opened after clicking on " \
                                                "Nav Bar Item!"
    attach_screenshot(driver)

    assert newsfeed_page_base.is_user_can_like_default_post(), \
        "[Newsfeed Page] User can not like posts on Newsfeed Page!"
    assert newsfeed_page_base.is_user_can_unlike_default_post(),\
        "[Newsfeed Page] User can not unlike posts on Newsfeed Page!"


@pytest.mark.skip
def test_case_fifteen(mobile_driver_opening_and_closing, email, password):
    COMMENT = 'just a comment'

    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    user_page_base = dashboard_page_base.click_user_avatar()
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking on User Avatar!"
    attach_screenshot(driver)

    USERNAME = user_page_base.get_username()
    user_page_base.click_back_button()
    dashboard_page_base = init_page_or_uiobject(driver, DashboardPageBase)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    newsfeed_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.NEWSFEED)
    assert newsfeed_page_base.is_page_opened(), "[Newsfeed Page] Newsfeed Page is not opened after clicking on " \
                                                "Nav Bar Item!"
    attach_screenshot(driver)

    comments_page_base = newsfeed_page_base.click_comment_button()
    assert comments_page_base.is_page_opened(), "[Comments Page] Comments Page is not opened " \
                                                "after clicking Comment Button!"
    attach_screenshot(driver)

    comments_page_base.send_comment(COMMENT)
    assert comments_page_base.is_comment_sent_by_username(COMMENT, USERNAME), "[Comments Page] Comment {} was " \
                                                                              "not sent by {}".format(COMMENT, USERNAME)
    attach_screenshot(driver)


@pytest.mark.skip
def test_case_sixteen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on " \
                                            "Nav Bar Item!"
    attach_screenshot(driver)

    settings_page_base = more_page_base.click_option(MoreMenuOption.SETTINGS)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened!"
    attach_screenshot(driver)

    privacy_center_page_base = settings_page_base.click_settings_page_option(SettingsItem.PRIVACY_CENTER)
    assert privacy_center_page_base.is_page_opened(), "[Privacy Center Page] Privacy Center Page is not opened!"
    attach_screenshot(driver)

    sharing_privacy_sett_page_base = \
        privacy_center_page_base.click_privacy_center_option(PrivacyCenterItem.SHARING_AND_PRIVACY_SETTINGS)
    assert sharing_privacy_sett_page_base.is_page_opened(), "[Sharing and Privacy Settings Page] Sharing and Privacy " \
                                                            "Settings Page is not opened!"
    attach_screenshot(driver)

    newsfeed_sharing_page_base = \
        sharing_privacy_sett_page_base.click_sharing_privacy_option(SharingPrivacyItem.NEWS_FEED_SHARING)
    assert newsfeed_sharing_page_base.is_page_opened(), "[Newsfeed Sharing Page] Newsfeed Sharing Page is not opened!"
    attach_screenshot(driver)

    assert newsfeed_sharing_page_base.is_option_checked(
        NewsfeedSharingItem.THERE_ARE_NEW_ARTICLES_FROM_THE_MYFITNESSPAL_BLOG), "[Newsfeed Sharing Page] " \
        "Option {} is not checked!".format(NewsfeedSharingItem.THERE_ARE_NEW_ARTICLES_FROM_THE_MYFITNESSPAL_BLOG)

    newsfeed_sharing_page_base.click_back_button()
    sharing_privacy_sett_page_base = init_page_or_uiobject(driver, SharingPrivacySettingsPageBase)
    assert sharing_privacy_sett_page_base.is_page_opened(), "[Sharing and Privacy Settings Page] Sharing and Privacy " \
                                                            "Settings Page is not opened!"

    sharing_privacy_sett_page_base.click_back_button()
    privacy_center_page_base = init_page_or_uiobject(driver, PrivacyCenterPageBase)
    assert privacy_center_page_base.is_page_opened(), "[Privacy Center Page] Privacy Center Page is not opened!"

    privacy_center_page_base.click_back_button()
    settings_page_base = init_page_or_uiobject(driver, SettingsPageBase)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened!"

    settings_page_base.click_back_button()
    more_page_base = init_page_or_uiobject(driver, MorePageBase)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened"

    newsfeed_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.NEWSFEED)
    assert newsfeed_page_base.is_page_opened(), "[Newsfedd Page] Newsfeed Page is not opened after clicking on " \
                                            "Nav Bar Item!"
    attach_screenshot(driver)

    assert newsfeed_page_base.is_articles_myfitnesspal_present(), "[Newsfeed Page] MyFitnessPal articles " \
                                                                  "are not present!"

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on " \
                                            "Nav Bar Item!"
    attach_screenshot(driver)

    settings_page_base = more_page_base.click_option(MoreMenuOption.SETTINGS)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened!"
    attach_screenshot(driver)

    privacy_center_page_base = settings_page_base.click_settings_page_option(SettingsItem.PRIVACY_CENTER)
    assert privacy_center_page_base.is_page_opened(), "[Privacy Center Page] Privacy Center Page is not opened!"
    attach_screenshot(driver)

    sharing_privacy_sett_page_base = \
        privacy_center_page_base.click_privacy_center_option(PrivacyCenterItem.SHARING_AND_PRIVACY_SETTINGS)
    assert sharing_privacy_sett_page_base.is_page_opened(), "[Sharing and Privacy Settings Page] Sharing and Privacy " \
                                                            "Settings Page is not opened!"
    attach_screenshot(driver)

    newsfeed_sharing_page_base = \
        sharing_privacy_sett_page_base.click_sharing_privacy_option(SharingPrivacyItem.NEWS_FEED_SHARING)
    assert newsfeed_sharing_page_base.is_page_opened(), "[Newsfeed Sharing Page] Newsfeed Sharing Page is not opened!"
    attach_screenshot(driver)

    newsfeed_sharing_page_base.uncheck_option(NewsfeedSharingItem.THERE_ARE_NEW_ARTICLES_FROM_THE_MYFITNESSPAL_BLOG)
    newsfeed_sharing_page_base.click_back_button()
    sharing_privacy_sett_page_base = init_page_or_uiobject(driver, SharingPrivacySettingsPageBase)
    assert sharing_privacy_sett_page_base.is_page_opened(), "[Sharing and Privacy Settings Page] Sharing and Privacy " \
                                                            "Settings Page is not opened!"

    sharing_privacy_sett_page_base.click_back_button()
    privacy_center_page_base = init_page_or_uiobject(driver, PrivacyCenterPageBase)
    assert privacy_center_page_base.is_page_opened(), "[Privacy Center Page] Privacy Center Page is not opened!"

    privacy_center_page_base.click_back_button()
    settings_page_base = init_page_or_uiobject(driver, SettingsPageBase)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened!"

    settings_page_base.click_back_button()
    more_page_base = init_page_or_uiobject(driver, MorePageBase)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened"

    newsfeed_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.NEWSFEED)
    assert newsfeed_page_base.is_page_opened(), "[Newsfedd Page] Newsfeed Page is not opened after clicking on " \
                                                "Nav Bar Item!"
    attach_screenshot(driver)

    assert not newsfeed_page_base.is_articles_myfitnesspal_present(), "[Newsfeed Page] MyFitnessPal articles " \
                                                                  "are not present!"
@pytest.mark.skip
def test_case_seventeen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on " \
                                             "Nav Bar Item!"
    attach_screenshot(driver)

    plans_page_base.click_filterby_button(FilterByButton.WORKOUT)
    plan_details_page_base = plans_page_base.click_on_plan(PlansPageItem.TOTAL_BODY_POWER)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.TOTAL_BODY_POWER), \
        "[Plan Details Page] Opened wrong plan! Expected {}".format(PlansPageItem.TOTAL_BODY_POWER)
    attach_screenshot(driver)


@pytest.mark.skip
def test_case_eighteen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    plans_page_base.click_filterby_button(FilterByButton.WORKOUT)
    plan_details_page_base = plans_page_base.click_on_plan(PlansPageItem.TOTAL_BODY_POWER)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.TOTAL_BODY_POWER), \
        "[Plan Details Page] Opened wrong plan! Expected {}".format(PlansPageItem.TOTAL_BODY_POWER)
    attach_screenshot(driver)

    about_plan_page_base = plan_details_page_base.click_start_button_zero_plans()
    assert about_plan_page_base.is_page_opened(), "[About Plan Page] About Plan Page is not opened " \
                                                  "after choosing and start plan!"
    attach_screenshot(driver)

    about_plan_page_base.click_continue_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking Continue Button!"
    assert plans_page_base.is_plan_shows(PlansPageItem.TOTAL_BODY_POWER), "[Plans Page] Not found needed title for plan! " \
                                                                   "Should be {}"\
                                                                    .format(PlansPageItem.TOTAL_BODY_POWER.value[0])
    attach_screenshot(driver)

    log_workout_page_base = plans_page_base.click_log_workout_button()
    assert log_workout_page_base.is_page_opened(), "[Log Workout Page] Log Workout Page is not opened"
    attach_screenshot(driver)

    log_workout_page_base.click_checkmark()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking " \
                                             "checkmark on Log Workout Page!"
    assert plans_page_base.is_workout_logged_confirmation_message_present(), \
        "[Plans Page] Workout Logged confirmation message is not present!"
    attach_screenshot(driver)


def test_case_nineteen(mobile_driver_opening_and_closing, email, password):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    plans_page_base.click_filterby_button(FilterByButton.WORKOUT)
    plan_details_page_base = plans_page_base.click_on_plan(PlansPageItem.TOTAL_BODY_POWER)
    assert plan_details_page_base.is_page_opened(), "[Plan Details Page] Plan Details Page is not opened!"
    assert plan_details_page_base.is_needed_plan_opened(PlansPageItem.TOTAL_BODY_POWER), \
        "[Plan Details Page] Opened wrong plan! Expected {}".format(PlansPageItem.TOTAL_BODY_POWER)
    attach_screenshot(driver)

    about_plan_page_base = plan_details_page_base.click_start_button_zero_plans()
    assert about_plan_page_base.is_page_opened(), "[About Plan Page] About Plan Page is not opened " \
                                                  "after choosing and start plan!"
    attach_screenshot(driver)

    about_plan_page_base.click_continue_button()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking Continue Button!"
    assert plans_page_base.is_plan_shows(
        PlansPageItem.TOTAL_BODY_POWER), "[Plans Page] Not found needed title for plan! " \
                                         "Should be {}" \
        .format(PlansPageItem.TOTAL_BODY_POWER.value[0])
    attach_screenshot(driver)

    log_workout_page_base = plans_page_base.click_log_workout_button()
    assert log_workout_page_base.is_page_opened(), "[Log Workout Page] Log Workout Page is not opened"
    attach_screenshot(driver)

    log_workout_page_base.click_checkmark()
    plans_page_base = init_page_or_uiobject(driver, PlansPageBase)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking " \
                                             "checkmark on Log Workout Page!"
    assert plans_page_base.is_workout_logged_confirmation_message_present(), \
        "[Plans Page] Workout Logged confirmation message is not present!"

    diary_page_base = plans_page_base.click_view_button()
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking View button!"
    attach_screenshot(driver)

    assert diary_page_base.is_workout_logged(), "[Diary Page] Workout is not logged!"
    attach_screenshot(driver)

