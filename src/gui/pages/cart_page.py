from src.gui.enums.products import Product
from src.gui.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

link = "https://www.saucedemo.com/cart.html"

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get(link)
        self.continue_shopping_button = None
        self.checkout_button = None

    def is_opened(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "continue-shopping")))
        self.continue_shopping_button = self.driver.find_element(By.ID, "continue-shopping")
        self.checkout_button = self.driver.find_element(By.ID, "checkout")
        return self.checkout_button.is_displayed() and self.continue_shopping_button.is_displayed()

    def is_product_link_present(self, product: Product):
        product_link = self.driver.find_element(By.XPATH, f"//div[text()='{product.value[0]}']")
        return product_link, f"[Cart Page] Product named {product.value[0]} is not present!"

    # def get_product_link_text(self, product: Product):
    #     product_link = self.driver.find_element(By.XPATH, f"//div[text()='{product.value}']")
    #     assert product_link, f"[Cart Page] Product named {product.value} is not present!"
    #     return product_link.text

    def get_product_price(self, product: Product):
        product_price = self.driver.find_element(By.XPATH,
                                                      f"//div[text()='{product.value[0]}']/../following-sibling::div/div")
        assert product_price, f"[Cart Page] Price for product named {product.value[0]} is not present!"
        tmp_price = product_price.text[1:]
        return float(tmp_price)

    def click_continue_shopping(self):
        self.continue_shopping_button.click()


