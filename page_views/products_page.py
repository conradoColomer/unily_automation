from selenium.webdriver.common.by import By
from page_views.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_NAME = (By.XPATH, "//div[@class='productinfo text-center']//p[text()='Winter Top']/ancestor::div[@class='productinfo text-center']")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "add-to-cart")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "button.btn-success.close-modal")
    QUANTITY_FIELD = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@class='btn btn-default cart' and contains(text(), 'Add to cart')]")

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def get_all_product_names(self):
        elements = self.wait_for_element(self.PRODUCT_NAME)
        return [element.text for element in elements]

    def is_product_name_visible(self):
        element = self.wait_for_element(self.PRODUCT_NAME)  # Espera a que el elemento esté presente
        return element.is_displayed()  # Verifica si el elemento está visible

    def click_first_two_add_to_cart_buttons(self):
        buttons = self.wait_for_elements(
            (By.CSS_SELECTOR, "a.add-to-cart[data-product-id='1'], a.add-to-cart[data-product-id='2']"))

        for button in buttons[:2]:
            # Espera a que el botón sea clickeable
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
            button.click()
            self.click_continue_shopping_button()  # Hace clic en "Continue Shopping" después de cada clic en "Add to Cart"

    def click_continue_shopping_button(self):
        button = self.wait_for_element(self.CONTINUE_SHOPPING_BUTTON)
        # Espera a que el botón sea clickeable y hace clic en él
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(button))
        button.click()

    def enter_quantity(self, quantity):
        self.enter_text(self.QUANTITY_FIELD, quantity)

    def add_product_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()
        self.click_continue_shopping_button()
