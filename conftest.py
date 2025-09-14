import pytest
from selene import browser

@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def setup_browser(request):
    browser.config.browser_name = request.param
    browser.config.base_url = 'https://github.com'
    browser.config.timeout = 5
    yield
    browser.quit()
