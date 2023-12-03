import pytest
from selenium import webdriver

@pytest.fixture()
def setupNya():
    driver= webdriver.Firefox()
    yield driver
    driver.quit()