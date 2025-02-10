# pages/home_page.py
from selenium.webdriver.common.by import By
from page_views.base_page import BasePage

class HomePage(BasePage):
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    EXPECTED_TITLE = "Automation Exercise"

    def navigate_to_products(self):
        self.click(self.PRODUCTS_BUTTON)

    def is_home_page_visible(self):
        return self.driver.title == self.EXPECTED_TITLE