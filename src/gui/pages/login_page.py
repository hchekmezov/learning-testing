from selenium import webdriver

from selenium.webdriver.common.by import By
from src.gui.pages.base_page import BasePage
from src.gui.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.saucedemo.com/"


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(link)
        self.username_field = None
        self.password_field = None
        self.login_button = None
        self.error_message = None

    def is_opened(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        self.username_field = self.driver.find_element(By.ID, "user-name")
        self.password_field = self.driver.find_element(By.ID, "password")
        self.login_button = self.driver.find_element(By.ID, "login-button")
        return self.username_field.is_displayed() and self.password_field.is_displayed()

    def is_error_message_present(self):
        self.error_message = self.driver.find_element(By.XPATH, '//div[@class=\'error-message-container error\']')
        return self.error_message

    def get_error_message_text(self):
        return self.error_message.text

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

