import pytest
from selenium import webdriver
from page_views.home_page import HomePage
from page_views.products_page import ProductsPage
from page_views.cart_page import CartPage

class TestAddProductsInCart:
    @pytest.fixture(scope="class")
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_add_products_in_cart(self, setup_class):
        self.driver.get("https://automationexercise.com")
        home_page = HomePage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)

        home_page.navigate_to_products()

        # Add first product to cart
        products_page.add_product_to_cart(1)
        products_page.continue_shopping()

        # Add second product to cart
        products_page.add_product_to_cart(2)
        products_page.view_cart()

        cart_products = cart_page.get_cart_products()
        assert len(cart_products) == 2