from selenium.webdriver.common.by import By
from page_views.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    EXPECTED_TITLE = "Automation Exercise"
    CART_LINK = (By.CSS_SELECTOR, "a[href='/view_cart']")
    VIEW_PRODUCT_LINK = (
    By.XPATH, "//a[text()='View Product']")

    def navigate_to_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def is_home_page_visible(self):
        return self.driver.title == self.EXPECTED_TITLE

    def navigate_to_cart(self):
        self.wait_for_element(self.CART_LINK).click()

    def view_product(self):
        # Espera a que el enlace "View Product" sea clickeable
        view_product_link = self.wait_for_element(self.VIEW_PRODUCT_LINK)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(view_product_link))
        view_product_link.click()



