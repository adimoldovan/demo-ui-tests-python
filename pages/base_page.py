from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def send_keys(self, selector, string):
        self.get_element(selector).send_keys(string)

    def click(self, selector):
        self.get_clickable_element(selector).click()

    def is_displayed(self, selector, timeout=1):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(expected_conditions.visibility_of_element_located(selector))
            return True
        except TimeoutException:
            return False

    def get_text(self, selector):
        return self.get_element(selector).text

    def get_element(self, selector):
        return self.wait.until(expected_conditions.visibility_of_element_located(selector),
                               "Timeout waiting for element with selector {} [timeout = {}s]".format(selector,
                                                                                                     self.timeout))

    def get_clickable_element(self, selector):
        return self.wait.until(expected_conditions.element_to_be_clickable(selector),
                               "Timeout waiting for clickable element with selector {} [timeout = {}s]".format(selector,
                                                                                                               self.timeout))
