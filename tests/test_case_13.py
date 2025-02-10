import pytest
from selenium import webdriver
from page_views.home_page import HomePage
from page_views.products_page import ProductsPage
from page_views.cart_page import CartPage


class TestVerifyProductQuantityInCart:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_verify_product_quantity_in_cart(self):
        self.driver.get("https://automationexercise.com")
        home_page = HomePage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)

        # Verificar que la página de inicio sea visible
        assert home_page.is_home_page_visible(), "La página de inicio no es visible"

        home_page.navigate_to_products()
        products_page.add_product_to_cart(1, quantity=4)  # Agregar 4 unidades del producto

        home_page.navigate_to_cart()
        assert cart_page.get_product_quantity(1) == 4, "La cantidad del producto en el carrito no es correcta"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()