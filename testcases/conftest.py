import pytest
from selenium import webdriver

from config import URL
from page_object.base import Base
from page_object.page_login import LoginPage


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Edge()
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(browser):
    login_page = LoginPage(browser)
    return login_page


# 失败时截图
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        login_page = item.funcargs.get("login_page")
        if login_page:
            login_page.screenshot("登录失败")
