import pytest
from selenium import webdriver
from page_views.home_page import HomePage
from page_views.products_page import ProductsPage

class TestSearchProduct:
    @pytest.fixture(scope="class")
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.quit()

    def test_search_product(self, setup_class):
        self.driver.get("https://automationexercise.com")
        home_page = HomePage(self.driver)
        products_page = ProductsPage(self.driver)

        # Verify that home page is visible successfully
        assert home_page.is_home_page_visible(), "Home page is not visible"

        home_page.navigate_to_products()
        products_page.search_product("Dress")

        product_names = products_page.get_all_product_names()
        assert all("Dress" in name for name in product_names)