from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class HeaderPage(BasePage):
    LOGIN_BTN = (By.CSS_SELECTOR, 'span > button.btn-link')
    PRODUCTS_NUMBER_BADGE = (By.CSS_SELECTOR, 'span.shopping_cart_badge')

    def open_login(self):
        self.click(self.LOGIN_BTN)
        return LoginPage(self.driver)

    def get_no_of_products(self):
        if self.is_displayed(self.PRODUCTS_NUMBER_BADGE):
            return int(self.get_text(self.PRODUCTS_NUMBER_BADGE))
        else:
            return 0
