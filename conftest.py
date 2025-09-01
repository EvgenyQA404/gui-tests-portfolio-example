import pytest
from selenium import webdriver


# Только chrome
@pytest.fixture(params=['chrome'])
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    browser = webdriver.Chrome(options=options)

    yield browser

    browser.quit()


# chrome и mozilla
# @pytest.fixture(params=['firefox', 'chrome'])
# def driver(request):
#     browser = None
#     options = webdriver.FirefoxOptions()
#     options.add_argument('--window-size=1920,1080')
#     if request.param == 'firefox':
#         browser = webdriver.Firefox(options=options)
#     elif request.param == 'chrome':
#         browser = webdriver.Chrome()
#
#     yield browser
#
#     browser.quit()
