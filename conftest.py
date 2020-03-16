import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
import chromedriver_autoinstaller

@pytest.fixture
def driver(request):
    chromedriver_autoinstaller.install()
    chrome_driver = WebDriver()
    chrome_driver.implicitly_wait(60)
    yield chrome_driver
    chrome_driver.close()
