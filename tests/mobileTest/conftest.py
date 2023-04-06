import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# desired_caps for MFP
# desired_caps = {
#     "deviceName": "samsung",
#     "platformName": "Android",
#     "version": "9.0",
#     "udid": "ce07182773284537017e",
#     # "udid": "emulator-5554",
#     "app": "/Users/glebchekmezov/Library/MobileTesting/MyFitnessPal-21-03-2023.apk",
#     "automationName": "uiautomator2",
#     "realDevice": True
# }

##############################################################################################

# desired_caps for Google Fit
desired_caps = {
    "deviceName": "samsung",
    "platformName": "Android",
    "version": "9.0",
    "udid": "ce07182773284537017e",
    # "udid": "emulator-5554",
    "app": "/Users/glebchekmezov/Library/MobileTesting/Fit_base.apk",
    "appPackage": "com.google.android.apps.fitness",
    "appActivity": "com.google.android.apps.fitness.welcome.WelcomeActivity",
    "automationName": "uiautomator2",
    "realDevice": True
    # "appWaitForLaunch": "false"
}


@pytest.fixture(scope='function')
def mobile_driver_opening_and_closing():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()

