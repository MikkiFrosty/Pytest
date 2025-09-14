import pytest
from selene import browser, be, have

DESKTOP = (1920, 1080)
MOBILE  = (375, 812)

DESKTOP_SIGN_IN = 'header a.HeaderMenu-link--sign-in'
MOBILE_SIGN_IN  = 'a[href="/login"]'

@pytest.mark.parametrize('size', [DESKTOP, MOBILE], ids=['desktop', 'mobile'])
def test_sign_in_with_parametrize(setup_browser, size):
    browser.config.window_width, browser.config.window_height = size
    browser.open('/')
    if size[0] >= 1200:
        browser.element(DESKTOP_SIGN_IN).should(be.visible).click()
    else:
        browser.element(MOBILE_SIGN_IN).should(be.visible).click()
    browser.should(have.url_containing('login'))

@pytest.mark.parametrize(
    'size',
    [
        pytest.param(DESKTOP, id='desktop'),
        pytest.param(MOBILE,  id='mobile', marks=pytest.mark.skip(reason='desktop only')),
    ],
)
def test_sign_in_desktop_only(setup_browser, size):
    browser.config.window_width, browser.config.window_height = size
    browser.open('/')
    browser.element(DESKTOP_SIGN_IN).should(be.visible).click()
    browser.should(have.url_containing('login'))

@pytest.mark.parametrize('size', [DESKTOP, MOBILE], ids=['desktop', 'mobile'])
def test_sign_in_mobile_only(setup_browser, size):
    if size[0] >= 1200:
        pytest.skip('mobile only')
    browser.config.window_width, browser.config.window_height = size
    browser.open('/')
    browser.element(MOBILE_SIGN_IN).should(be.visible).click()
    browser.should(have.url_containing('login'))
