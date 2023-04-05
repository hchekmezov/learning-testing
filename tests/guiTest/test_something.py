import logging
import time
import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from pytest_zebrunner import attach_test_artifact
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from src.gui.enums.burger_menu_buttons import BurgerButton
from src.gui.pages.login_page import LoginPage
from src.gui.pages.login_page import MainPage
from src.gui import constants
from src.gui.enums.products import Product
from pytest_zebrunner import attach_test_screenshot
from src.gui.enums.product_sort_option import ProductSortOption

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


def test_empty_credentials(driver_opening_and_closing):
    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened!"
    login_page.login("", "")
    assert login_page.is_error_message_present(), "[Login Page] Error message is not present while it should be!"
    assert login_page.get_error_message_text() == constants.ERROR_MESSAGE_USERNAME_REQUIRED, \
        f"[Login Page] Error message contains wrong text! " \
        f"Should be ***{constants.ERROR_MESSAGE_USERNAME_REQUIRED}***, " \
        f"but it ***{login_page.get_error_message_text()}***"


@pytest.mark.parametrize("username", [('standard_user'),
                                      ('locked_out_user'),
                                      ('problem_user'),
                                      ('performance_glitch_user')])
def test_wrong_username_or_password(driver_opening_and_closing, username):
    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened!"
    login_page.login(username, constants.PASSWORD + "prosto")
    assert login_page.is_error_message_present(), "[Login Page] Error message is not present while it should be!"
    assert login_page.get_error_message_text() == constants.ERROR_MESSAGE_WRONG_USERNAME_AND_PASSWORD, \
        f"[Login Page] Error message contains wrong text! " \
        f"Should be ***{constants.ERROR_MESSAGE_WRONG_USERNAME_AND_PASSWORD}***, " \
        f"but it ***{login_page.get_error_message_text()}***"


def test_add_to_cart(driver_opening_and_closing):
    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened!"
    login_page.login(constants.USERNAME, constants.PASSWORD)
    main_page = MainPage(driver)
    assert main_page.is_opened(), "[Main Page] Main Page is not opened after clicking login button!"
    main_page.add_to_cart(Product.SAUCE_LABS_BIKE_LIGHT)
    product_price_from_main_page = main_page.get_product_price(Product.SAUCE_LABS_BIKE_LIGHT)
    cart_page = main_page.open_cart_page()
    assert cart_page.is_opened(), "[Cart Page] Cart Page is not opened after clicking cart icon!"
    assert cart_page.is_product_link_present(Product.SAUCE_LABS_BIKE_LIGHT), \
        f"[Cart Page] Product Link named {Product.SAUCE_LABS_BIKE_LIGHT} is not present!"
    assert cart_page.get_product_price(Product.SAUCE_LABS_BIKE_LIGHT) \
           == product_price_from_main_page, \
        f"[Cart Page] Price for {Product.SAUCE_LABS_BIKE_LIGHT} is not equals with price on Main Page!"
    # cart_page.click_continue_shopping()
    # main_page = MainPage(driver)
    # assert main_page.is_opened(), "[Main Page] Main Page is not opened after clicking continue shopping button!"
    # burger_menu = main_page.open_burger_menu()
    # assert burger_menu.is_opened(), "[Burger Menu] Burger Menu is not opened after clicking burger button!"
    # burger_menu.click_button_from_menu(BurgerButton.LOGOUT)
    # login_page = LoginPage(driver)
    # assert login_page.is_opened(), "[Login Page] Login Page is not opened after clicking Logout Button!"


def test_open_product(driver_opening_and_closing):
    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened!"
    login_page.login(constants.USERNAME, constants.PASSWORD)
    main_page = MainPage(driver)
    assert main_page.is_opened(), "[Main Page] Main Page is not opened after clicking login button!"
    assert main_page.is_product_present(Product.SAUCE_LABS_FLEECE_JACKET), \
        f"[Main Page] Product named {Product.SAUCE_LABS_FLEECE_JACKET.value[0]} is not present!"
    product_price_main_page = main_page.get_product_price(Product.SAUCE_LABS_FLEECE_JACKET)
    product_page = main_page.open_product_page(Product.SAUCE_LABS_FLEECE_JACKET)
    assert product_page.is_opened(), "[Product Page] Product Page is not opened!"
    assert product_page.get_product_name() == Product.SAUCE_LABS_FLEECE_JACKET.value[0], \
        f"[Product Page] Product name on Product Page is {product_page.get_product_name()} while it should be " \
        f"{Product.SAUCE_LABS_FLEECE_JACKET.value[0]}"
    assert product_page.get_product_price() == product_price_main_page, f"[Product Page] Prices are not eqauls! " \
                                                                        f"On Main Page price " \
                                                                        f"is {product_price_main_page}, but on " \
                                                                        f"Product Page price " \
                                                                        f"is {product_page.get_product_price()}"
    product_page.click_back_to_products_button()
    main_page = MainPage(driver)
    assert main_page.is_opened(), "[Main Page] Main Page is not opened after clicking Back To Products button!"
    burger_menu = main_page.open_burger_menu()
    assert burger_menu.is_opened(), "[Burger Menu] Burger Menu is not opened after clicking burger button!"
    burger_menu.click_button_from_menu(BurgerButton.LOGOUT)
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened after clicking Logout Button!"


def test_sort_items(driver_opening_and_closing):
    driver = driver_opening_and_closing
    login_page = LoginPage(driver)
    assert login_page.is_opened(), "[Login Page] Login Page is not opened!"
    login_page.login(constants.USERNAME, constants.PASSWORD)
    main_page = MainPage(driver)
    assert main_page.is_opened(), "[Main Page] Main Page is not opened after clicking login button!"
    main_page.click_sort_option(ProductSortOption.AZ)
    current_list = main_page.get_list_product_names_text()
    sorted_list = sorted(current_list)
    assert current_list == sorted_list, f"[Main Page] Wrong alphabetic order ({ProductSortOption.AZ.value})!"
    main_page.click_sort_option(ProductSortOption.ZA)
    current_list = main_page.get_list_product_names_text()
    sorted_list.sort(reverse=True)
    assert current_list == sorted_list, f"[Main Page] Wrong alphabetic order! ({ProductSortOption.ZA.value})"
    main_page.click_sort_option(ProductSortOption.LOHI)
    current_list = main_page.get_list_product_prices_float()
    sorted_list = sorted(current_list)
    assert current_list == sorted_list, f"[Main Page] Wrong numeric order ({ProductSortOption.LOHI.value})!"
    main_page.click_sort_option(ProductSortOption.HILO)
    current_list = main_page.get_list_product_prices_float()
    sorted_list.sort(reverse=True)
    assert current_list == sorted_list, f"[Main Page] Wrong numeric order ({ProductSortOption.HILO.value})!"
