import logging

from selenium.webdriver.common.by import By
from src.gui.pages.base_page import BasePage
from src.gui.enums.products import Product
from pytest_zebrunner.zebrunner_logging import ZebrunnerHandler
from selenium.webdriver.support import expected_conditions as EC
from src.gui.pages.product_page import ProductPage
from src.gui.enums.product_sort_option import ProductSortOption

from src.gui.pages.burger_menu import BurgerMenu
from src.gui.pages.cart_page import CartPage

link = "https://www.saucedemo.com/inventory.html"
logger = logging.getLogger(__name__)
logger.addHandler(ZebrunnerHandler())
logger.setLevel(logging.INFO)


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(link)
        self.logo = None
        self.shopping_cart_link = None
        self.burger_button = None
        self.add_to_cart_button = None

    def is_opened(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))
        self.logo = self.driver.find_element(By.XPATH, "//div[@class='app_logo']")
        self.shopping_cart_link = self.driver.find_element(By.XPATH, "//a[@class=\"shopping_cart_link\"]")
        self.burger_button = self.driver.find_element(By.XPATH, "//div[@class='bm-burger-button']")
        return self.logo.is_displayed() and self.shopping_cart_link.is_displayed()

    def is_product_present(self, product: Product):
        return self.driver.find_element(By.XPATH, f"//div[text()='{product.value[0]}']")

    def add_to_cart(self, product: Product):
        self.add_to_cart_button = self.driver.find_element(By.XPATH,
                                                           f"//*[*[div[text()='{product.value[0]}']]]"
                                                           "/following-sibling::div//button")
        assert self.add_to_cart_button, f"[Main Page] Add to cart button named {product.value[0]} is not present!"
        self.add_to_cart_button.click()

    def open_cart_page(self):
        assert self.shopping_cart_link, "[Main Page] Shopping cart icon is not present!"
        self.shopping_cart_link.click()
        return CartPage(self.driver)

    # def get_product_link_text(self, product: Product):
    #     product_link = self.driver.find_element(By.XPATH, f"//div[text()='{product.value[0]}']")
    #     assert product_link, f"[Main Page] Product named {product.value[0]} is not present!"
    #     return product_link.text

    def get_product_price(self, product: Product):
        product_price = self.driver.find_element(By.XPATH,
                                                      f"//*[*[div[text()='{product.value[0]}']]]/following-sibling::div/div")
        assert product_price, f"[Main Page] Price for product named {product.value[0]} is not present!"
        tmp_price = product_price.text[1:]
        return float(tmp_price)

    def get_list_product_names_text(self):
        return [el.text for el in self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")]

    def get_list_product_prices_float(self):
        return [float(el.text[1:]) for el in self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")]

    # Maybe do not need
    def get_dictionary_name_and_price(self, list_names, list_price):
        res_dict = {}
        for i in range(len(list_price)):
            res_dict[list_names[i]] = list_price[i]
        return res_dict

    def open_product_page(self, product: Product):
        product_name = self.driver.find_element(By.XPATH, f"//div[text()='{product.value[0]}']")
        product_name.click()
        return ProductPage(self.driver, product)

    def open_burger_menu(self):
        self.burger_button.click()
        return BurgerMenu(self.driver)

    def click_sort_option(self, product_sort_option: ProductSortOption):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@class='product_sort_container']"))).click()
        option = self.driver.find_element(By.XPATH,
                                          f"//select[@class='product_sort_container']"
                                          f"/option[@value='{product_sort_option.value}']")
        option.click()



