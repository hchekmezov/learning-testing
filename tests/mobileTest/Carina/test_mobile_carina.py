from src.mobile.mobileTesting.Carina.pages.android.welcome_page import WelcomePage
from src.mobile.mobileTesting.Carina.pages.android.login_page import LoginPage
from src.mobile.mobileTesting.Carina.pages.android.web_view_page import WebViewPage
from src.mobile.mobileTesting.Carina.pages.android.navigate_up_menu import NavigateUpMenuPage
from src.mobile.mobileTesting.Carina.pages.android.map_page import MapPage
from src.mobile.mobileTesting.Carina.pages.android.ui_elements_page import UIElementsPage
from src.mobile.mobileTesting.Carina.enums.navigate_up_menu_item import NavigateUpMenuItem
from src.mobile.mobileTesting.Carina.enums.sex_radio_buttons import SexRadioButton
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from src.mobile.utils.direction import Direction

import logging

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


NAME = 'GLEB'
PASSWORD = 'CHEKMEZOV'


def test_carina_first(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    # element = driver.find_element()
    # element.is_displayed()
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    assert login_page.is_name_field_present(), "[Login Page] Name field is not present!"
    assert login_page.is_password_field_present(), "[Login Page] Password Field is not present!"
    assert login_page.is_sex_button_present(
        SexRadioButton.MALE), f"[Login Page] {SexRadioButton.MALE.value} is not present!"
    assert login_page.is_sex_button_present(
        SexRadioButton.FEMALE), f"[Login Page] {SexRadioButton.FEMALE.value} is not present!"
    assert login_page.is_privacy_policy_checkbox_present(), "[Login Page] Privacy Policy Checkbox is not present!"
    assert not login_page.is_sex_button_checked(
        SexRadioButton.MALE), f"[Login Page] {SexRadioButton.MALE.value} is checked while it should not be!"
    assert not login_page.is_sex_button_checked(
        SexRadioButton.FEMALE), f"[Login Page] {SexRadioButton.FEMALE.value} is checked while it should not be!"
    assert not login_page.is_privacy_policy_checked(), "[Login Page] Privacy Policy checked while it should not be!"
    login_page.send_name_and_password(NAME, PASSWORD)
    assert login_page.get_text_in_name_field() == NAME, "[Login Page] Text in name field typed wrong!"
    assert login_page.get_text_in_password_field() == PASSWORD, "[Login Page] Text in password field typed wrong!"
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    assert login_page.is_sex_button_checked(SexRadioButton.MALE), f"[Login Page] {SexRadioButton.MALE.value} is not checked while it should be!"
    login_page.check_privacy_policy()
    assert login_page.is_privacy_policy_checked(), "[Login Page] Privacy Checkbox is not checked while it should be!"
    login_page.click_sign_up_button()
    web_view_page = WebViewPage(driver)
    assert web_view_page.is_page_opened(), "[Web View Page] Web View Page is not opened!"


def test_carina_second(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    login_page.send_name_and_password(NAME, PASSWORD)
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    assert not login_page.is_sign_up_button_enabled(), "[Login Page] Sign up button in enabled while it should not be!"


def test_carina_third(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    login_page.send_name_and_password(NAME, PASSWORD)
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    login_page.check_privacy_policy()
    login_page.click_sign_up_button()
    web_view_page = WebViewPage(driver)
    assert web_view_page.is_page_opened(), "[Web View Page] Web View Page is not opened!"
    web_view_page.click_navigate_up_button()
    navigate_up_menu = NavigateUpMenuPage(driver)
    assert navigate_up_menu.is_page_opened(), \
        "[Navigate Up Menu Page] Navigate Up Menu Page is not opened after clicking navigate up button!"
    navigate_up_menu.click_navigate_up_menu_item(NavigateUpMenuItem.MAP)
    map_page = MapPage(driver)
    assert map_page.is_page_opened(), "[Map Page] Map Page is not opened after clicking Map Page Item!"


def test_carina_fourth(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    login_page.send_name_and_password(NAME, PASSWORD)
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    login_page.check_privacy_policy()
    login_page.click_sign_up_button()
    web_view_page = WebViewPage(driver)
    assert web_view_page.is_page_opened(), "[Web View Page] Web View Page is not opened!"
    web_view_page.click_navigate_up_button()
    navigate_up_menu = NavigateUpMenuPage(driver)
    assert navigate_up_menu.is_page_opened(), \
        "[Navigate Up Menu Page] Navigate Up Menu Page is not opened after clicking navigate up button!"
    navigate_up_menu.click_navigate_up_menu_item(NavigateUpMenuItem.UI_ELEMENTS)
    ui_elements_page = UIElementsPage(driver)
    assert ui_elements_page.is_page_opened(), "[UI Elements Page] UI Elements Page is not opened after clicking UI elements Page Item"


def test_carina_fifth(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    login_page.send_name_and_password(NAME, PASSWORD)
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    login_page.check_privacy_policy()
    login_page.click_sign_up_button()
    web_view_page = WebViewPage(driver)
    assert web_view_page.is_page_opened(), "[Web View Page] Web View Page is not opened!"
    web_view_page.click_navigate_up_button()
    navigate_up_menu = NavigateUpMenuPage(driver)
    assert navigate_up_menu.is_page_opened(), \
        "[Navigate Up Menu Page] Navigate Up Menu Page is not opened after clicking navigate up button!"
    navigate_up_menu.click_navigate_up_menu_item(NavigateUpMenuItem.UI_ELEMENTS)
    ui_elements_page = UIElementsPage(driver)
    assert ui_elements_page.is_page_opened(), "[UI Elements Page] UI Elements Page is not opened after clicking UI elements Page Item"
    # deviceSize = driver.get_window_size()
    # screenWidth = deviceSize['width']
    # screenHeight = deviceSize['height']
    assert ui_elements_page.is_enable_switch_present(), "[UI Elements Page] Enable Switch is not present!"


def test_carina_sixth(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    welcome_page = WelcomePage(driver)
    assert welcome_page.is_page_opened(), "[Welcome Page] Welcome Page is not opened!"
    welcome_page.click_next_button()
    login_page = LoginPage(driver)
    assert login_page.is_page_opened(), "[Login Page] Login Page is not opened after clicking Next Button!"
    login_page.send_name_and_password(NAME, PASSWORD)
    login_page.check_sex_radio_button(SexRadioButton.MALE)
    login_page.check_privacy_policy()
    login_page.click_sign_up_button()
    web_view_page = WebViewPage(driver)
    assert web_view_page.is_page_opened(), "[Web View Page] Web View Page is not opened!"
    web_view_page.image_view_swipe_n_times(4, Direction.LEFT)

