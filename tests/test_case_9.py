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
        products_page.search_product("Dress")

        product_names = products_page.get_all_product_names()
        assert all("Dress" in name for name in product_names), "No todos los productos encontrados contienen 'Dress' en el nombre"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()