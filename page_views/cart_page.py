from selenium.webdriver.common.by import By
from page_views.base_page import BasePage

class CartPage(BasePage):
    CART_PRODUCTS = (By.XPATH, "//tr[@class='cart_product']")
    PRODUCT_QUANTITY = (By.XPATH, "//button[@class='disabled']")

    def get_cart_products(self):
        return self.wait_for_element(self.CART_PRODUCTS)

    def get_product_quantity(self):
        element = self.wait_for_element(self.PRODUCT_QUANTITY)
        return element.text