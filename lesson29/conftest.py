import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome():
    s = ChromeService(r'chromedriver.exe')
    # settings driver for win 64
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def firefox(request):
    # settings driver for win
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def chrome_class(request):
    s = ChromeService(r'chromedriver.exe')
    # settings driver for win 64
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    driver.implicitly_wait(5)
    yield driver
    driver.quit()