import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging


@pytest.fixture(scope="session")
def session_setup():
    # region setup
    logging.debug('Session setup')
    yield ChromeDriverManager().install()
    # endregion

    # region teardown
    logging.debug('Session teardown')
    # endregion


@pytest.fixture(scope="function")
def driver_setup(request, session_setup):
    # region setup
    logging.debug('Driver setup')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1920x1080')

    if os.environ.get('CI') or request.config.getoption('--headless'):
        chrome_options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(session_setup), options=chrome_options)
    driver.get('https://adimoldovan.github.io/demo-shop/#/')

    request.cls.driver = driver

    yield driver
    # endregion

    # region tear down
    logging.debug('Driver teardown')
    driver.quit()
    # endregion


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help="Run browser in headless mode")


def pytest_exception_interact(node, report):
    """Called when an exception was raised"""

    if report.failed:
        screenshots_path = 'reports/screenshots'
        name = ".".join(node.nodeid.split("::")[-2:])
        Path(screenshots_path).mkdir(parents=True, exist_ok=True)
        screenshot_file = f"{screenshots_path}/{name}.png"

        try:
            node.funcargs['driver_setup'].get_screenshot_as_file(screenshot_file)
            logging.debug(f"Screenshot saved as '{screenshot_file}'")
        except Exception as ex:
            logging.error(f"Exception saving screenshot {ex}")


def pytest_configure(config):
    logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel('WARNING')
    logging.getLogger('urllib3.connectionpool').setLevel('WARNING')
    logging.getLogger('requests_oauthlib').setLevel('WARNING')
    logging.getLogger('oauthlib').setLevel('WARNING')

    if os.environ.get('CI'):
        config.option.log_cli_level = 'error'
