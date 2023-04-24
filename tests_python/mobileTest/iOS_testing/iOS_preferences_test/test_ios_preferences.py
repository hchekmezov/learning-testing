from src.mobile.mobileTesting.iOS_testing.iOS_preferences.preferences_page import PreferencesPage


def test_preferences(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    driver.activate_app("com.apple.Preferences")
    preferences_page = PreferencesPage(driver)
    preferences_page.click_general_button()
    driver.back()