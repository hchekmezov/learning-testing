from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.MFP.pages.commons.diary_page.edit_diary_page_base import EditDiaryPageBase
from src.mobile.utils.initialize_utils import init_page_or_uiobject
from src.mobile.utils.mobile_utils import EC


class EditDiaryPage(EditDiaryPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__select_all_checkbox = (AppiumBy.ID, "com.myfitnesspal.android:id/select_all")
        self.__action_bar_title = (AppiumBy.ID, "com.myfitnesspal.android:id/action_bar_title")
        self.__trash_bin_button = (AppiumBy.ACCESSIBILITY_ID, "Delete")

        self.__delete_panel = (AppiumBy.ID, "com.myfitnesspal.android:id/action_bar_root")
        self.__delete_on_delete_panel = (AppiumBy.ID, "android:id/button1")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__action_bar_title)) \
            and WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__select_all_checkbox))

    def delete_all_items(self):
        self.driver.find_element(*self.__select_all_checkbox).click()
        self.driver.find_element(*self.__trash_bin_button).click()
        assert WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.__delete_panel)), \
            "[Edit Diary Page] Delete Panel is not present after clicking trash bin button!"
        self.driver.find_element(*self.__delete_on_delete_panel).click()


