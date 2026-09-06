import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://arjitnigam.github.io/myDreams/")

    yield driver

    driver.quit()