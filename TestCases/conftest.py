import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path= "C:\chromedriver.exe")

    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path= "C:\geckodriver.exe")

    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://admin-demo.nopcommerce.com/login")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    #driver.close()