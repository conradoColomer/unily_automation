from selenium.webdriver.common.by import By
from page_views.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    PRODUCT_NAME = (By.XPATH, "//div[@class='productinfo text-center']//p[text()='Winter Top']/ancestor::div[@class='productinfo text-center']")
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "add-to-cart")

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