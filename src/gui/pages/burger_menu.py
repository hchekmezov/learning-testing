from src.gui.enums.burger_menu_buttons import BurgerButton
from src.gui.pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import logging
from selenium.webdriver.common.by import By
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class BurgerMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.about = None
        self.logout = None

    def is_opened(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        self.about = self.driver.find_element(By.ID, "about_sidebar_link")
        self.logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        return self.about.is_displayed() and self.logout.is_displayed()

    def click_button_from_menu(self, burger_button: BurgerButton):
        if burger_button == BurgerButton.LOGOUT:
            self.logout.click()
