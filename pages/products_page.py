from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'div.card button.btn-link')

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
