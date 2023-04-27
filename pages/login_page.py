from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_FLD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FLD = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.btn-primary')

    def login(self, username, password):
        self.send_keys(self.USERNAME_FLD, username)
        self.send_keys(self.PASSWORD_FLD, password)
        self.click(self.LOGIN_BTN)
