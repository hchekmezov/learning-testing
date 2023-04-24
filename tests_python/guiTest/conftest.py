import pytest

from selenium import webdriver


@pytest.fixture(scope='function')
def driver_opening_and_closing():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.close()
