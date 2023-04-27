import pytest

from pages.header_page import HeaderPage


@pytest.mark.usefixtures("driver_setup")
@pytest.mark.authentication
class TestAuthentication:
    def test_login(self):
        header = HeaderPage(self.driver)
        login_page = header.open_login()
        login_page.login('dino', 'choochoo')

        # todo assert login successful
