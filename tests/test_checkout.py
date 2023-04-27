import os

import pytest

from pages.header_page import HeaderPage
from pages.products_page import ProductsPage


@pytest.mark.usefixtures("driver_setup")
@pytest.mark.checkout
class TestCheckout:
    def test_checkout(self):
        header = HeaderPage(self.driver)
        initial_no_of_products = header.get_no_of_products()
        products_page = ProductsPage(self.driver)
        products_page.add_product_to_cart()
        actual_no_of_products = header.get_no_of_products()

        if os.environ.get('FAIL_DEMO'):
            actual_no_of_products += 1

        assert actual_no_of_products == initial_no_of_products + 1, "Unexpected number of products in cart!"
