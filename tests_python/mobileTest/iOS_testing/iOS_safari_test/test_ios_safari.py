from src.mobile.mobileTesting.iOS_testing.iOS_safari.sauce_page import SaucePage


def test_safari(mobile_driver_opening_and_closing):
    driver = mobile_driver_opening_and_closing
    sauce_page = SaucePage(driver)
    driver.get("http://saucelabs.com/test/guinea-pig")
    sauce_page.verify_element_text()