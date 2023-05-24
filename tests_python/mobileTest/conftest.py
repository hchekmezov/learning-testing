import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# desired_caps for iOS
# desired_caps = {
#     "deviceName": "IPhone",
#     "platformName": "iOS",
#     "version": "16.2",
#     "udid": "9A856D0A-3E48-4611-9E9C-21BF9C1B1FA6",
#     "app": "com.apple.mobilesafari",
#     "automationName": "XCUITest",
#     "realDevice": True
# }


# desired_caps for MFP
desired_caps = {
    "deviceName": "samsung",
    "platformName": "Android",
    "version": "9.0",
    # "udid": "ce07182773284537017e",
    "udid": "emulator-5554",
    # "app": "/Users/glebchekmezov/Library/MobileTesting/MyFitnessPal-21-03-2023.apk",
    "app": "https://www.googleapis.com/drive/v3/files/1T8TGoDIdml2MBW-MUn5m46G_qiJk4nxx?alt=media&key=AIzaSyBaC4EPP_FnI5u6Xwx-eZFvizk_a11yyvI",
    "automationName": "uiautomator2",
    "realDevice": True
}

##############################################################################################

# desired_caps for Google Fit
# desired_caps = {
#     "deviceName": "samsung",
#     "platformName": "Android",
#     "version": "9.0",
#     "udid": "ce07182773284537017e",
#     # "udid": "emulator-5554",
#     "app": "/Users/glebchekmezov/Library/MobileTesting/Fit_base.apk",
#     "appPackage": "com.google.android.apps.fitness",
#     "appActivity": "com.google.android.apps.fitness.welcome.WelcomeActivity",
#     "automationName": "uiautomator2",
#     "realDevice": True
#     # "appWaitForLaunch": "false"
# }


def pytest_addoption(parser):
    parser.addoption("--email", action="store", default="default email")
    parser.addoption("--password", action="store", default="default password")


@pytest.fixture(scope="session")
def email(request):
    email_value = request.config.option.email
    if email_value is None:
        pytest.skip()
    return email_value


@pytest.fixture(scope="session")
def password(request):
    password_value = request.config.option.password
    if password_value is None:
        pytest.skip()
    return password_value


@pytest.fixture(scope='function')
def mobile_driver_opening_and_closing():
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


# DRIVER CAPABILITIES EXAMPLE:
# {
# 	'platform': 'LINUX',
# 	'webStorageEnabled': False,
# 	'takesScreenshot': True,
# 	'javascriptEnabled': True,
# 	'databaseEnabled': False,
# 	'networkConnectionEnabled': True,
# 	'locationContextEnabled': False,
# 	'warnings':
# 	{},
# 	'desired':
# 	{
# 		'platformName': 'Android',
# 		'browserVersion': '9.0',
# 		'deviceName': 'samsung',
# 		'udid': 'ce07182773284537017e',
# 		'app': '/Users/glebchekmezov/Library/MobileTesting/MyFitnessPal-21-03-2023.apk',
# 		'automationName': 'uiautomator2',
# 		'realDevice': True
# 	},
# 	'platformName': 'Android',
# 	'browserVersion': '9.0',
# 	'deviceName': 'ce07182773284537017e',
# 	'udid': 'ce07182773284537017e',
# 	'app': '/Users/glebchekmezov/Library/MobileTesting/MyFitnessPal-21-03-2023.apk',
# 	'automationName': 'uiautomator2',
# 	'realDevice': True,
# 	'deviceUDID': 'ce07182773284537017e',
# 	'appPackage': 'com.myfitnesspal.android',
# 	'deviceApiLevel': 28,
# 	'platformVersion': '9',
# 	'deviceScreenSize': '1080x2220',
# 	'deviceScreenDensity': 420,
# 	'deviceModel': 'SM-N9500',
# 	'deviceManufacturer': 'samsung',
# 	'pixelRatio': 2.625,
# 	'statBarHeight': 63,
# 	'viewportRect':
# 	{
# 		'left': 0,
# 		'top': 63,
# 		'width': 1080,
# 		'height': 2118
# 	}
# }

