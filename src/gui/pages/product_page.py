import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.gui.pages.base_page import BasePage
from src.gui.enums.products import Product
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from pytest_zebrunner import attach_test_screenshot

link = "https://www.saucedemo.com/inventory-item.html?id={0}"

logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class ProductPage(BasePage):

    def __init__(self, driver, product: Product):
        super().__init__(driver)
        self.driver = driver
        # self.driver.save_screenshot("screenshots/screenshot1.png")
        # attach_test_screenshot("screenshots/screenshot1.png")
        # logger.info(link.format(product.value[1]))
        self.driver.get(link.format(product.value[1]))
        # self.driver.save_screenshot("screenshots/screenshot2.png")
        # attach_test_screenshot("screenshots/screenshot2.png")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class=\"inventory_details_name large_size\"]")))
        self.name = self.driver.find_element(By.XPATH, "//div[@class=\"inventory_details_name large_size\"]")
        self.price = self.driver.find_element(By.XPATH, "//div[@class=\"inventory_details_price\"]")
        self.back_to_products = self.driver.find_element(By.ID, "back-to-products")

    def is_opened(self):
        return self.name.is_displayed() and self.price.is_displayed()

    def get_product_name(self):
        return self.name.text

    def get_product_price(self):
        tmp_price = self.price.text[1:]
        return float(tmp_price)

    def click_back_to_products_button(self):
        self.back_to_products.click()