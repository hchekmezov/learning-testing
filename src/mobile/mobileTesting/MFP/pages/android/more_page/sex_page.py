from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.enums.more_page.sex_options import SexOption
from src.mobile.utils.mobile_utils import EC

from src.mobile.mobileTesting.MFP.pages.commons.more_page.sex_page_base import SexPageBase


class SexPage(SexPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__needed_sex = None
        self.__title = (AppiumBy.ID, "com.myfitnesspal.android:id/alertTitle")
        self.__set_button = (AppiumBy.ID, "android:id/button1")
        self.__cancel_button = (AppiumBy.ID, "android:id/button2")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__set_button))

    def set_sex(self, sex: SexOption):
        self.__needed_sex = (AppiumBy.XPATH, "//*[@resource-id='com.myfitnesspal.android:id/text' and @text='{}']"
                                             "/preceding-sibling::android.widget.RadioButton".format(sex.value))
        self.driver.find_element(*self.__needed_sex).click()
        self.driver.find_element(*self.__set_button).click()

