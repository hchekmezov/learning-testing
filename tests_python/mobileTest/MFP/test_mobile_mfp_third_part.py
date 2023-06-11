import logging
import pytest
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.dashboard_page.activity_level import ActivityLevel
from src.mobile.mobileTesting.MFP.enums.dashboard_page.goals_options import GoalsOption
from src.mobile.mobileTesting.MFP.enums.dashboard_page.weekly_goal_items import WeeklyGoalItem
from src.mobile.mobileTesting.MFP.enums.more_page.edit_profile_options import EditProfileOption
from src.mobile.mobileTesting.MFP.enums.more_page.more_menu_options import MoreMenuOption
from src.mobile.mobileTesting.MFP.enums.more_page.settings_items import SettingsItem
from src.mobile.mobileTesting.MFP.enums.more_page.sex_options import SexOption
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.acitivity_level_page_base import ActivityLevelPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.current_weight_page_base import CurrentWeightPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.goal_weight_page_base import GoalWeightPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.goals_page_base import GoalsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.sure_page_base import SurePageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.user_page_base import UserPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page.weekly_goal_page_base import WeeklyGoalPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.date_page_base import DatePageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.edit_profile_page_base import EditProfilePageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.height_page_base import HeightPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.more_page_base import MorePageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.settings_page_base import SettingsPageBase
from src.mobile.mobileTesting.MFP.pages.commons.more_page.sex_page_base import SexPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import attach_screenshot
from tests_python.mobileTest.MFP.test_mobile_mfp import login_to_dashboard

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def test_case_twenty(mobile_driver_opening_and_closing, email, password):
    FIRST_GOAL = 1712
    SECOND_GOAL = 1412


    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver, email, password)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"

    attach_screenshot(driver)

    user_page_base = dashboard_page_base.click_user_avatar()
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking on User Avatar!"

    attach_screenshot(driver)

    goals_page_base = user_page_base.click_update_goals_button()
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened!"

    attach_screenshot(driver)

    goals_page_base.click_option(GoalsOption.ACTIVITY_LEVEL)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on activity level!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    activity_level_page_base = init_page_or_uiobject(driver, ActivityLevelPageBase)
    assert activity_level_page_base.is_page_opened(), "[Activity Level Page] Activity Level Page is not opened " \
                                                      "after clicking yes button!"
    attach_screenshot(driver)

    activity_level_page_base.set_activity_level(ActivityLevel.ACTIVE)
    goals_page_base = init_page_or_uiobject(driver, GoalsPageBase)
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened after setting Activity Level!"

    attach_screenshot(driver)

    goals_page_base.click_option(GoalsOption.CURRENT_WEIGHT)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on current weight!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    current_weight_page_base = init_page_or_uiobject(driver, CurrentWeightPageBase)
    assert current_weight_page_base.is_page_opened(), "[Current Weight Page] Current Weight Page is not opened!"

    attach_screenshot(driver)

    current_weight_page_base.set_weight(70)
    goals_page_base = init_page_or_uiobject(driver, GoalsPageBase)
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened after setting current weight!"

    attach_screenshot(driver)

    ##################

    goals_page_base.click_option(GoalsOption.GOAL_WEIGHT)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on goal weight!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    goal_weight_page_base = init_page_or_uiobject(driver, GoalWeightPageBase)
    assert goal_weight_page_base.is_page_opened(), "[Goal Weight Page] Goal Weight Page is not opened!"

    attach_screenshot(driver)

    goal_weight_page_base.set_weight(60)
    goals_page_base = init_page_or_uiobject(driver, GoalsPageBase)
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened after setting goal weight!"

    attach_screenshot(driver)

    #########

    ##################

    goals_page_base.click_option(GoalsOption.WEEKLY_GOAL)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on weekly goal!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    weekly_goal_page = init_page_or_uiobject(driver, WeeklyGoalPageBase)
    assert weekly_goal_page.is_page_opened(), "[Weekly Goal Page] Weekly Goal Page is not opened!"

    attach_screenshot(driver)

    weekly_goal_page.set_weekly_goal(WeeklyGoalItem.ZERO_FIVE_KG_WEEK)
    goals_page_base = init_page_or_uiobject(driver, GoalsPageBase)
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened after setting Activity Level!"

    attach_screenshot(driver)

    #########

    goals_page_base.click_back_button()
    user_page_base = init_page_or_uiobject(driver, UserPageBase)
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking back button!"

    attach_screenshot(driver)

    user_page_base.click_back_button()
    dashboard_page_base = init_page_or_uiobject(driver, DashboardPageBase)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened after clicking " \
                                                 "back button!"

    attach_screenshot(driver)

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on " \
                                            "Nav Bar Item!"
    attach_screenshot(driver)

    settings_page_base = more_page_base.click_option(MoreMenuOption.SETTINGS)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened after clicking {}"\
        .format(MoreMenuOption.SETTINGS)

    attach_screenshot(driver)

    edit_profile_page_base = settings_page_base.click_settings_page_option(SettingsItem.EDIT_PROFILE)
    assert edit_profile_page_base.is_page_opened(), "[Edit Profile Page] Edit Profile Page is not opened after " \
                                                    "clicking {}".format(SettingsItem.EDIT_PROFILE)

    attach_screenshot(driver)
    #####
    edit_profile_page_base.click_option(EditProfileOption.SEX)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on sex!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    sex_page_base = init_page_or_uiobject(driver, SexPageBase)
    assert sex_page_base.is_page_opened(), "[Sex Page] Sex Page is not opened!"

    attach_screenshot(driver)

    sex_page_base.set_sex(SexOption.FEMALE)
    edit_profile_page_base = init_page_or_uiobject(driver, EditProfilePageBase)
    assert edit_profile_page_base.is_page_opened(), "[Edit Profile Page] Edit Profile Page is not opened after " \
                                                    "setting Sex!"

    attach_screenshot(driver)

    edit_profile_page_base.click_option(EditProfileOption.HEIGHT)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on height!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    height_page_base = init_page_or_uiobject(driver, HeightPageBase)
    assert height_page_base.is_page_opened(), "[Height Page] Height Page is not opened!"

    attach_screenshot(driver)

    height_page_base.set_height(160)
    edit_profile_page_base = init_page_or_uiobject(driver, EditProfilePageBase)
    assert edit_profile_page_base.is_page_opened(), "[Edit Profile Page] Edit Profile Page is not opened after " \
                                                    "setting Height!"

    attach_screenshot(driver)

    edit_profile_page_base.click_option(EditProfileOption.DATE_OF_BIRTH)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on date of birth!"

    attach_screenshot(driver)

    sure_page_base.click_yes_button()
    date_page_base = init_page_or_uiobject(driver, DatePageBase)
    assert date_page_base.is_page_opened(), "[Date Page] Date Page is not opened!"

    attach_screenshot(driver)

    date_page_base.switch_to_text_mode()
    date_page_base.set_date_by_years_ago(25)
    edit_profile_page_base = init_page_or_uiobject(driver, EditProfilePageBase)
    assert edit_profile_page_base.is_page_opened(), "[Edit Profile Page] Edit Profile Page is not opened after " \
                                                    "setting Date of Birth!"

    attach_screenshot(driver)

    edit_profile_page_base.click_back_button()
    settings_page_base = init_page_or_uiobject(driver, SettingsPageBase)
    assert settings_page_base.is_page_opened(), "[Settings Page] Settings Page is not opened after clicking " \
                                                "Back Button!"

    settings_page_base.click_back_button()
    more_page_base = init_page_or_uiobject(driver, MorePageBase)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking Back Button!"

    dashboard_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DASHBOARD)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"

    user_page_base = dashboard_page_base.click_user_avatar()
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking on User Avatar!"

    assert user_page_base.get_number_of_daily_goal() == FIRST_GOAL, "[User Page] User goals not equal, shoulb be {}" \
                                                                    ", but actual {}".format(FIRST_GOAL,
                                                                                             user_page_base
                                                                                            .get_number_of_daily_goal())

    attach_screenshot(driver)

    goals_page_base = user_page_base.click_update_goals_button()
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened!"

    goals_page_base.click_option(GoalsOption.WEEKLY_GOAL)
    sure_page_base = init_page_or_uiobject(driver, SurePageBase)
    assert sure_page_base.is_page_opened(), "[Sure Page] Sure Page is not opened after clicking on weekly goal!"

    sure_page_base.click_yes_button()
    weekly_goal_page = init_page_or_uiobject(driver, WeeklyGoalPageBase)
    assert weekly_goal_page.is_page_opened(), "[Weekly Goal Page] Weekly Goal Page is not opened!"

    weekly_goal_page.set_weekly_goal(WeeklyGoalItem.ZERO_SEVENTY_FIVE_KG_WEEK)
    goals_page_base = init_page_or_uiobject(driver, GoalsPageBase)
    assert goals_page_base.is_page_opened(), "[Goals Page] Goals Page is not opened after setting Activity Level!"

    goals_page_base.click_back_button()
    user_page_base = init_page_or_uiobject(driver, UserPageBase)
    assert user_page_base.is_page_opened(), "[User Page] User Page is not opened after clicking back button!"

    assert user_page_base.get_number_of_daily_goal() == SECOND_GOAL, "[User Page] User goals not equal, shoulb be {}" \
                                                                    ", but actual {}".format(SECOND_GOAL,
                                                                                             user_page_base
                                                                                            .get_number_of_daily_goal())

    attach_screenshot(driver)
