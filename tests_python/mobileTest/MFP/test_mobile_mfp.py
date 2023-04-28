import time

import pytest

from src.common_utils.soft_assert import SoftAssert
from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.custom_summary_item import CustomSummaryItem
from src.mobile.mobileTesting.MFP.enums.diary_activity_items import DiaryActivityItem
from src.mobile.mobileTesting.MFP.enums.meals_names import MealName
from src.mobile.mobileTesting.MFP.enums.more_menu_options import MoreMenuOption
from src.mobile.mobileTesting.MFP.enums.my_prem_tools_items import MyPremToolsItem
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.add_food_page_base import AddFoodPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.existing_user_tutor_page_base import ExistingUserTutorPageBase
from src.mobile.mobileTesting.MFP.pages.commons.login_page_base import LoginPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.preview_page_base import PreviewPageBase
from src.mobile.utils.constants import Constants
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


# TESTS AND METHORD BEFORE 20.04.2023
@pytest.mark.skip
def test_mfp_first(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page = init_page_or_uiobject(driver, MFPCommonPageBase)
    preview_page = init_page_or_uiobject(driver, PreviewPageBase)
    assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    preview_page.click_login_button()
    login_page = init_page_or_uiobject(driver, LoginPageBase)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    # login_page.type_email_and_password(configs.get("email").data, configs.get("password").data)
    login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    login_page.click_login_button()
    assert mfp_common_page.wait_until_spinner_rounding(), \
        "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
    existing_user_tutor_page = init_page_or_uiobject(driver, ExistingUserTutorPageBase)
    assert existing_user_tutor_page.is_page_opened(), \
        "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
    existing_user_tutor_page.click_close_button()
    dashboard_page = init_page_or_uiobject(driver, DashboardPageBase)
    assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"

@pytest.mark.skip
def test_mfp_second(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page = init_page_or_uiobject(driver, MFPCommonPageBase)
    preview_page = init_page_or_uiobject(driver, PreviewPageBase)
    assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    preview_page.click_login_button()
    login_page = init_page_or_uiobject(driver, LoginPageBase)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    login_page.click_login_button()
    assert mfp_common_page.wait_until_spinner_rounding(), \
        "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
    existing_user_tutor_page = init_page_or_uiobject(driver, ExistingUserTutorPageBase)
    assert existing_user_tutor_page.is_page_opened(), \
        "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
    existing_user_tutor_page.click_close_button()
    dashboard_page = init_page_or_uiobject(driver, DashboardPageBase)
    assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    dashboard_page.click_track_steps_button()
    steps_page = init_page_or_uiobject(driver, StepsPageBase)
    assert steps_page.is_page_opened(), "[Steps Page] Steps Page is not opened after clicking Track Steps Button"
    steps_page.click_enable_checkbox()
    assert steps_page.is_progress_spinner_rounding_present()

# TESTS AND METHODS AFTER 20.04.2023 (MAJOR UPDATE BY init_page_or_uiobject)

def login_to_dashboard(driver) -> DashboardPageBase:
    preview_page_base = init_page_or_uiobject(driver, PreviewPageBase)
    assert preview_page_base.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    login_page_base = preview_page_base.click_login_button()
    assert login_page_base.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    login_page_base.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page_base.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    existing_user_tutor_page_base = login_page_base.click_login_button()
    if existing_user_tutor_page_base.is_page_opened():
        return existing_user_tutor_page_base.click_close_button()
    else:
        return init_page_or_uiobject(driver, DashboardPageBase)

###############
# MY TEST CASES
###############

def test_mfp_third(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)
    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)
    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)
    nutrition_page_base = diary_page_base.open_nutrition_page()
    assert nutrition_page_base.is_page_opened(), "[Nutrition Page] Nutrition Page is not opened after clicking " \
                                                 "Nutrition Button!"
    attach_screenshot(driver)

def test_mfp_fourth(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)
    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)
    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)
    diary_page_base.click_add_button_on_activity(DiaryActivityItem.BREAKFAST)
    add_food_page_base = init_page_or_uiobject(driver, AddFoodPageBase)
    assert add_food_page_base.is_page_opened(), "[Add Food Page] Even abstract Add Food Page is not opened!"
    assert add_food_page_base.is_needed_page_opened_by_meal_name(MealName.BREAKFAST), \
        "[Add Food Page] Add Food Page is not opened for needed item! Needed {}, Actual {}"\
            .format(MealName.BREAKFAST, add_food_page_base.get_title())
    attach_screenshot(driver)
    add_food_page_base.find_and_add_meal('meatball')
    attach_screenshot(driver)
    add_food_page_base.click_back_button()
    diary_page_base = init_page_or_uiobject(driver, DiaryPageBase)
    attach_screenshot(driver)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after driver.back()!"
    assert diary_page_base.is_meal_added(), "[Diary Page] Meal was not added!"
    diary_page_base.delete_all_added_meals_in_activity(DiaryActivityItem.BREAKFAST)
    assert diary_page_base.is_all_meals_deleted_in_activity(DiaryActivityItem.BREAKFAST), \
        "[Diary Page] Not all added meals deleted in activity {}".format(DiaryActivityItem.BREAKFAST)


################
# IRA'S TEST CASES
###############


def test_case_one(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    newsfeed_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.NEWSFEED)
    assert newsfeed_page_base.is_page_opened(), \
        "[Newsfeed Page] Newsfeed Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    plans_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.PLANS)
    assert plans_page_base.is_page_opened(), "[Plans Page] Plans Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)


def test_case_two(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    assert diary_page_base.is_calories_remaining_chosen(), "[Diary Page] Calories Remaining is not chosen!"
    diary_page_base.clear_user_diary()

    goal = diary_page_base.get_calories_goal_int_value()
    remaining = diary_page_base.get_calories_remaining_int_value()
    assert goal == remaining, "[Diary Page] Calories Goal Value is not the same to Calories Remaining Value! " \
                              "Goal: {}, Remaining: {}".format(goal, remaining)

def test_case_three(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    driver.hide_keyboard()
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    more_button_page_base = diary_page_base.click_more_button_on_activity(DiaryActivityItem.BREAKFAST)
    assert more_button_page_base.is_page_opened(), \
        "[More Button Page] More Button Page is not opened after clicking more button!"
    quick_add_page_base = more_button_page_base.click_quick_add_button()
    assert quick_add_page_base.is_page_opened(), \
        "[Quick Add Page] Quick Add Page is not opened after clicking Quick add button!"
    quick_add_page_base.quick_add_fat_carbs_protein(1, 1, 1)
    assert quick_add_page_base.is_calories_equals_value(17), "[Quick Add Page] Calories value is not equals 17!"

def test_case_five(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    custom_dashboard_page_base = diary_page_base.click_summary_more_button()
    assert custom_dashboard_page_base.is_page_opened(), "[Custom Dashboard Page] Custom Dashboard Page is not " \
                                                        "opened after clicking summary more button!"
    custom_summary_page_base = custom_dashboard_page_base.click_custom_summary_button()
    assert custom_summary_page_base.is_page_opened(), "[Custom Summary Page] Custom Summary Page is not opened " \
                                                      "after clicking custom summary button"
    nutrients = [CustomSummaryItem.FAT, CustomSummaryItem.CARBOHYDRATES, CustomSummaryItem.PROTEIN]

    # SOFT ASSERT
    soft_assert = SoftAssert()
    for nutrient in nutrients:
        soft_assert.assertExperession(custom_summary_page_base.is_nutrient_checked(nutrient),
                                          "[Custom Summary Page] Nutrient {} is not checked!".format(nutrient.get_title()))
    soft_assert.assertAll()


def test_case_six(mobile_driver_opening_and_closing):
    SELECTED_3_OF_3 = '3 of 3 nutrients selected.'
    SELECTED_4_OF_3 = '4 nutrients selected. Please select only 3.'
    SELECTED_2_OF_3 = '2 of 3 nutrients selected.'

    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
    assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    custom_dashboard_page_base = diary_page_base.click_summary_more_button()
    assert custom_dashboard_page_base.is_page_opened(), "[Custom Dashboard Page] Custom Dashboard Page is not " \
                                                        "opened after clicking summary more button!"
    attach_screenshot(driver)
    custom_summary_page_base = custom_dashboard_page_base.click_custom_summary_button()
    assert custom_summary_page_base.is_page_opened(), "[Custom Summary Page] Custom Summary Page is not opened " \
                                                      "after clicking custom summary button"
    attach_screenshot(driver)
    txt = custom_summary_page_base.get_nutrient_selected_text()
    assert txt == SELECTED_3_OF_3, "[Custom Summary Page] Selected Text is wrong! Expected: {}, Actual: {}"\
        .format(SELECTED_3_OF_3, txt)
    attach_screenshot(driver)
    assert custom_summary_page_base.is_save_button_active(), "[Custom Summary Page] Save button is not active!"
    custom_summary_page_base.uncheck_nutrient(CustomSummaryItem.FAT)
    txt = custom_summary_page_base.get_nutrient_selected_text()
    assert txt == SELECTED_2_OF_3, "[Custom Summary Page] Selected Text is wrong! Expected: {}, Actual: {}" \
        .format(SELECTED_2_OF_3, txt)
    attach_screenshot(driver)
    assert not custom_summary_page_base.is_save_button_active(), "[Custom Summary Page] Save button is active!"
    nutrients = [CustomSummaryItem.FAT, CustomSummaryItem.IRON]
    for nutrient in nutrients:
        custom_summary_page_base.check_nutrient(nutrient)
    txt = custom_summary_page_base.get_nutrient_selected_text()
    assert txt == SELECTED_4_OF_3, "[Custom Summary Page] Selected Text is wrong! Expected: {}, Actual: {}" \
        .format(SELECTED_4_OF_3, txt)
    attach_screenshot(driver)
    assert not custom_summary_page_base.is_save_button_active(), "[Custom Summary Page] Save button is active!"


def test_case_seven(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

#    SOFT ASSERT
    soft_assert = SoftAssert()
    lst_of_options = list(MoreMenuOption.__members__.values())
    for option in lst_of_options:
        soft_assert.assertExperession(more_page_base.is_option_present(option),
                                          "[More Page] Option {} is not present!".format(option.value))

    soft_assert.assertAll()


def test_case_eight(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing

    mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)

    dashboard_page_base = login_to_dashboard(driver)
    assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
    attach_screenshot(driver)

    more_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.MORE)
    assert more_page_base.is_page_opened(), "[More Page] More Page is not opened after clicking on Nav Bar Item!"
    attach_screenshot(driver)

    my_prem_tools_page_base = more_page_base.click_option(MoreMenuOption.MY_PREMIUM_TOOLS)
    assert my_prem_tools_page_base.is_page_opened(), "[My Premium Tools Page] My Premium Tools Page is not opened " \
                                                     "after clicking {} option".format(MoreMenuOption.MY_PREMIUM_TOOLS)
    attach_screenshot(driver)
    soft_assert = SoftAssert()
    lst_of_tools_items = list(MyPremToolsItem.__members__.values())
    for item in lst_of_tools_items:
        soft_assert.assertExperession(my_prem_tools_page_base.is_option_and_description_displayed(item),
                                      "[My Premium Tools Page] Item {} is not displayed!".format(item))

    soft_assert.assertAll()
















