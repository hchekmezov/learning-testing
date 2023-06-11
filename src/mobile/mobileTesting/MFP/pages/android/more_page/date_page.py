from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from src.mobile.utils.mobile_utils import EC
from datetime import datetime, timedelta

from src.mobile.mobileTesting.MFP.pages.commons.more_page.date_page_base import DatePageBase


class DatePage(DatePageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__title_picker = (AppiumBy.ID, "com.myfitnesspal.android:id/mtrl_picker_title_text")
        self.__ok_button = (AppiumBy.ID, "com.myfitnesspal.android:id/confirm_button")
        self.__cancel_button = (AppiumBy.ID, "com.myfitnesspal.android:id/cancel_button")
        self.__switcher = (AppiumBy.ID, "com.myfitnesspal.android:id/mtrl_picker_header_toggle")

        self.__month_navigation = (AppiumBy.ID, "com.myfitnesspal.android:id/month_navigation_fragment_toggle")
        self.__input_date = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id"
                                             "/mtrl_picker_text_input_date']//android.widget.EditText")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title_picker)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__ok_button))

    def switch_to_text_mode(self):
        try:
            self.driver.find_element(*self.__input_date)
        except:
            self.driver.find_element(*self.__switcher).click()

    def set_date_by_years_ago(self, years: int):
        current_date = datetime.now()
        new_date = current_date - timedelta(days=years * 365.25)  # Учитываем високосные года
        formatted_date = new_date.strftime("%-m/%d/%y")
        self.driver.find_element(*self.__input_date).clear().send_keys(formatted_date)
        self.driver.find_element(*self.__ok_button).click()


