import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from data import UserData


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для создания WebDriver (Chrome и Firefox)"""
    browser = request.param
    
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
    
    yield driver
    driver.quit()


@pytest.fixture
def test_email():
    """Email тестового пользователя (можно переопределить через STELLAR_EMAIL)"""
    return os.getenv("STELLAR_EMAIL", UserData.EMAIL)


@pytest.fixture
def test_password():
    """Пароль тестового пользователя (можно переопределить через STELLAR_PASSWORD)"""
    return os.getenv("STELLAR_PASSWORD", UserData.PASSWORD)
