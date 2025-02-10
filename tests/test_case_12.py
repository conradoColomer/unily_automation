import pytest
from selenium import webdriver
from page_views.home_page import HomePage
from page_views.products_page import ProductsPage
from page_views.cart_page import CartPage

# Clase de prueba para agregar productos al carrito
class TestAddProductsInCart:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_add_products_to_cart(self):
        self.driver.get("https://automationexercise.com")
        home_page = HomePage(self.driver)
        products_page = ProductsPage(self.driver)
        cart_page = CartPage(self.driver)

        # Verificar que la página de inicio sea visible
        assert home_page.is_home_page_visible(), "La página de inicio no es visible"

        home_page.navigate_to_products()

        products_page.click_first_two_add_to_cart_buttons()

        # Navegar al carrito y verificar que los productos están agregados
       # home_page.navigate_to_cart()
       # assert cart_page.is_product_in_cart(1), "El primer producto no está en el carrito"
       # assert cart_page.is_product_in_cart(2), "El segundo producto no está en el carrito"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()