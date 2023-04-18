from appium.webdriver.common.appiumby import AppiumBy

from src.mobile.mobileTesting.GoogleFit.enums.home_page.home_page_block_title import HomePageBlockTitle
from src.mobile.mobileTesting.GoogleFit.enums.home_page.home_page_first_titles import FirstTitles
from src.mobile.mobileTesting.GoogleFit.enums.nav_container_buttons import NavContainerButton
from src.mobile.mobileTesting.GoogleFit.pages.android.gf_common_page import GFCommonPage
from src.mobile.mobileTesting.GoogleFit.pages.android.plus_button_modal import PlusButtonModal
from src.mobile.mobileTesting.GoogleFit.pages.commons.home_page_base import HomePageBase
from src.mobile.utils.mobile_utils import *
from src.mobile.utils.operating_system import OS
from selenium.webdriver.remote.webelement import WebElement


class HomePage(HomePageBase):

    def __init__(self, driver: Remote):
        super().__init__(driver)
        self.__lottie_celebration = (AppiumBy.ID, "com.google.android.apps.fitness:id/lottie_celebration")
        self.__plus_button = (AppiumBy.ID, "com.google.android.apps.fitness:id/add_entry_fab")
        self.__cards_frame_container = (AppiumBy.ID, "com.google.android.apps.fitness:id/cards_frame")
        self.__learn_more = (AppiumBy.XPATH, "//android.widget.Button[@text='Learn more']")
        self.__title_of_material_card = (
            AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/material_card']"
                            "//*[@text='{}']")
        self.__playlist_carousel = (AppiumBy.ID, "com.google.android.apps.fitness:id/playlist_carousel")
        # self.__playlist_item_title = (
        #     AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/playlist_carousel']"
        #                     "//*[@text='{}']")
        self.__playlist_button_title = (
            AppiumBy.XPATH, "//*[@resource-id='com.google.android.apps.fitness:id/playlist_button']"
                            "//*[@resource-id='com.google.android.apps.fitness:id/title']")

        self.__account_image = (AppiumBy.ID, "com.google.android.apps.fitness:id/og_apd_internal_image_view")

         # colors
        self.__card_custom_chart_title = (AppiumBy.ID, "com.google.android.apps.fitness:id/card_custom_chart_title")

    def is_page_opened(self) -> bool:
        return self.wait.until(EC.visibility_of_element_located(self.__lottie_celebration)) \
            and GFCommonPage(self.driver) \
                .get_bottom_nav_container() \
                .is_nav_container_button_selected(NavContainerButton.HOME)

    def get_plus_button(self):
        return PlusButtonModal(self.driver)

    def is_plus_button_static(self):
        return self.get_plus_button() \
            .is_plus_button_static_on_page(self.__learn_more, self.driver.find_element(*self.__cards_frame_container))

    def is_plus_button_present(self):
        return self.get_plus_button().is_present()

    def is_plus_button_below_container(self):
        return self.get_plus_button() \
            .is_plus_button_below_container_on_page(self.driver.find_element(*self.__cards_frame_container))

    def is_block_by_title_present(self, title: HomePageBlockTitle):
        return swipeToElementUpWithCount(
            (self.__title_of_material_card[0], self.__title_of_material_card[1].format(title.value)),
            10,
            self.driver,
            OS.ANDROID)

    def get_list_of_playlist_titles(self):
        result_list_of_titles = list()
        for i in range(10):
            swipeLeftInContainer(self.driver.find_element(*self.__playlist_carousel),
                                 1000,
                                 self.driver,
                                 OS.ANDROID)
            web_elements: list[WebElement] = self.driver.find_elements(*self.__playlist_button_title)
            # web_elements = self.driver.find_elements(*self.__playlist_button_title)
            for item in web_elements:
                if item.text not in result_list_of_titles:
                    result_list_of_titles.append(item.text)
            # result_list_of_titles.append(item.text for item in web_elements if item.text not in result_list_of_titles)
            # does not work :(
        return result_list_of_titles

    def click_plus_button(self):
        self.driver.find_element(*self.__plus_button).click()

    def get_color_of_account_image(self):
        return GFCommonPage(self.driver).get_color_of_element(self.__account_image)



