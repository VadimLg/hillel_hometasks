import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def chrome():
    s = Service(r'C:\Users\kva\PycharmProjects\hillel_hometasks\lesson19\chromedriver.exe')
    # settings driver for win 64
    driver = webdriver.Chrome(service=s)
    yield driver
    driver.quit()
