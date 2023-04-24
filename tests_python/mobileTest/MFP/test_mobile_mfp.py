from src.mobile.mobileTesting.MFP.enums.bottom_nav_bar_item import BottomNavBarItem
from src.mobile.mobileTesting.MFP.enums.diary_activity_items import DiaryActivityItem
from src.mobile.mobileTesting.MFP.enums.meals_names import MealName
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.add_food_page_base import AddFoodPageBase
from src.mobile.mobileTesting.MFP.pages.commons.dashboard_page_base import DashboardPageBase
from src.mobile.mobileTesting.MFP.pages.commons.diary_page.diary_page_base import DiaryPageBase
from src.mobile.mobileTesting.MFP.pages.commons.mfp_common_page_base import MFPCommonPageBase
from src.mobile.mobileTesting.MFP.pages.commons.preview_page_base import PreviewPageBase
from src.mobile.utils.constants import Constants
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import *

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


# TESTS AND METHORD BEFORE 20.04.2023
# @pytest.mark.skip
# def test_mfp_first(mobile_driver_opening_and_closing):
#     driver = mobile_driver_opening_and_closing
#     mfp_common_page = init_page_or_uiobject(driver, MFPCommonPageBase)
#     preview_page = init_page_or_uiobject(driver, PreviewPageBase)
#     assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
#     preview_page.click_login_button()
#     login_page = init_page_or_uiobject(driver, LoginPageBase)
#     assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
#     # login_page.type_email_and_password(configs.get("email").data, configs.get("password").data)
#     login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
#     assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
#     login_page.click_login_button()
#     assert mfp_common_page.wait_until_spinner_rounding(), \
#         "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
#     existing_user_tutor_page = init_page_or_uiobject(driver, ExistingUserTutorPageBase)
#     assert existing_user_tutor_page.is_page_opened(), \
#         "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
#     existing_user_tutor_page.click_close_button()
#     dashboard_page = init_page_or_uiobject(driver, DashboardPageBase)
#     assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
#
# @pytest.mark.skip
# def test_mfp_second(mobile_driver_opening_and_closing):
#     driver = mobile_driver_opening_and_closing
#     mfp_common_page = init_page_or_uiobject(driver, MFPCommonPageBase)
#     preview_page = init_page_or_uiobject(driver, PreviewPageBase)
#     assert preview_page.is_page_opened(), "[Preview Page] Preview Page is not opened!"
#     preview_page.click_login_button()
#     login_page = init_page_or_uiobject(driver, LoginPageBase)
#     assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
#     login_page.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
#     assert login_page.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
#     login_page.click_login_button()
#     assert mfp_common_page.wait_until_spinner_rounding(), \
#         "[Progress Spinner] Progress Spinner rouding too long after clicking Log In Button!"
#     existing_user_tutor_page = init_page_or_uiobject(driver, ExistingUserTutorPageBase)
#     assert existing_user_tutor_page.is_page_opened(), \
#         "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
#     existing_user_tutor_page.click_close_button()
#     dashboard_page = init_page_or_uiobject(driver, DashboardPageBase)
#     assert dashboard_page.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
#     dashboard_page.click_track_steps_button()
#     steps_page = init_page_or_uiobject(driver, StepsPageBase)
#     assert steps_page.is_page_opened(), "[Steps Page] Steps Page is not opened after clicking Track Steps Button"
#     steps_page.click_enable_checkbox()
#     assert steps_page.is_progress_spinner_rounding_present()

# TESTS AND METHODS AFTER 20.04.2023 (MAJOR UPDATE BY init_page_or_uiobject)

def login_to_dashboard(driver) -> DashboardPageBase:
    preview_page_base = init_page_or_uiobject(driver, PreviewPageBase)
    assert preview_page_base.is_page_opened(), "[Preview Page] Preview Page is not opened!"
    login_page_base = preview_page_base.click_login_button()
    assert login_page_base.is_page_opened(), "[Login Page] Login Page is not opened after clicking Log In Button!"
    login_page_base.type_email_and_password(Constants.EMAIL.value, Constants.PASSWORD.value)
    assert login_page_base.is_login_button_enabled(), "[Login Page] Log In Button should be enabled after typing email and password!"
    existing_user_tutor_page_base = login_page_base.click_login_button()
    assert existing_user_tutor_page_base.is_page_opened(), \
        "[Existing User Tutorial Page] Existing User Tutorial Page is not opened after clicking Log In Button!"
    return existing_user_tutor_page_base.click_close_button()

# def test_mfp_third(mobile_driver_opening_and_closing):
#     driver = mobile_driver_opening_and_closing
#     mfp_common_page_base = init_page_or_uiobject(driver, MFPCommonPageBase)
#     dashboard_page_base = login_to_dashboard(driver)
#     assert dashboard_page_base.is_page_opened(), "[Dashboard Page] Dashboard Page is not opened!"
#     attach_screenshot(driver)
#     diary_page_base = mfp_common_page_base.get_bottom_nav_bar().click_on_nav_bar_item(BottomNavBarItem.DIARY)
#     assert diary_page_base.is_page_opened(), "[Diary Page] Diary Page is not opened after clicking on Nav Bar Item!"
#     attach_screenshot(driver)
#     nutrition_page_base = diary_page_base.open_nutrition_page()
#     assert nutrition_page_base.is_page_opened(), "[Nutrition Page] Nutrition Page is not opened after clicking " \
#                                                  "Nutrition Button!"
#     attach_screenshot(driver)

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






