from appium.webdriver import Remote
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from src.mobile.mobileTesting.API_Demos.enums.popup_menu_button_items import PopupMenuButtonItem
from src.mobile.mobileTesting.API_Demos.pages.commons.start_page.api_demos_page.views_page.popup_menu_page_base import \
    PopupMenuPageBase
from src.mobile.utils.mobile_utils import EC


class PopupMenuPage(PopupMenuPageBase):
    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__make_button = (AppiumBy.XPATH, "//android.widget.Button[@text='MAKE A POPUP!']")
        # self.__toast = (AppiumBy.XPATH, "//android.widget.Toast")

    def is_page_opened(self) -> bool:
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.__make_button))

    def make_a_toast_for(self, item: PopupMenuButtonItem):
        self.driver.find_element(*self.__make_button).click()
        self.driver.implicitly_wait(0.7)
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/title' and @text='{}']"
                                 .format(item.value)).click()

    def is_toast_shown_for(self, item: PopupMenuButtonItem):
        toast = (AppiumBy.XPATH, "//android.widget.Toast[@text='Clicked popup menu item {}']".format(item.value))
        try:
            self.driver.find_element(*toast)
            return True
        except NoSuchElementException:
            return False





