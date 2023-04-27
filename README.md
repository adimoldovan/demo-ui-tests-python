# demo-ui-tests-python
UI automation demo with python, Selenium Webdriver, Pytest

```
# install virtualenv
pip install virtualenv

# create virtual environment
mkvirtualenv demo-ui-tests-python -p $(which python3)

# install dependencies
pip install -r requirements.txt

# run tests
pytest

# force a failed test
FAIL_DEMO=true pytest

# run a suite
pytest -m checkout

# headless
pytest --headless 
# OR
CI=true pytest

```

