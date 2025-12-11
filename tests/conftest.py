import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions


@pytest.fixture
def driver():
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver

    try:
        driver.terminate_app("com.schibsted.bomnegocio.androidApp")
    except Exception:
        pass
    try:
        driver.quit()
    except Exception:
        pass
