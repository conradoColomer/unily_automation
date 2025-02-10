import pytest
from selenium import webdriver
from page_views.home_page import HomePage
from page_views.products_page import ProductsPage
class TestSearchProduct:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_search_product(self):
        self.driver.get("https://automationexercise.com")
        home_page = HomePage(self.driver)
        products_page = ProductsPage(self.driver)

        # Verificar que la página de inicio sea visible
        assert home_page.is_home_page_visible(), "La página de inicio no es visible"

        home_page.navigate_to_products()
        products_page.search_product("Winter top")

        # Verificar que el producto 'Winter Top' esté visible
        assert products_page.is_product_name_visible(), "El producto 'Winter Top' no está visible"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()