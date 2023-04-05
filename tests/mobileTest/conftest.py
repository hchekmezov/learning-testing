import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_caps = {
    "deviceName": "samsung",
    "platformName": "Android",
    "version": "9.0",
    "udid": "ce07182773284537017e",
    "app": "/Users/glebchekmezov/Downloads/MyFitnessPal-21-03-2023.apk",
    "automationName": "uiautomator2",
    "realDevice": True
}


@pytest.fixture(scope='function')
def mobile_driver_opening_and_closing():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

