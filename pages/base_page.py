import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    def _get_wait(self, timeout=None):
        """Вернуть WebDriverWait с нужным таймаутом."""
        if timeout is None:
            return self.wait
        return WebDriverWait(self.driver, timeout)

    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)

    def is_element_visible(self, locator, timeout=None):
        """Проверить видимость элемента на странице"""
        try:
            self._get_wait(timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def find_visible_element(self, locator, timeout=None):
        """Найти видимый элемент на странице"""
        return self._get_wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator, timeout=None):
        """Найти кликабельный элемент на странице"""
        return self._get_wait(timeout).until(EC.element_to_be_clickable(locator))

    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url

    def check_url(self, expected_url_part):
        """Проверить, что URL содержит ожидаемую часть"""
        return expected_url_part in self.get_current_url()

    def wait_for_element_invisible(self, locator, timeout=None):
        """Дождаться, пока элемент станет невидимым"""
        return self._get_wait(timeout).until(EC.invisibility_of_element_located(locator))

    @staticmethod
    def normalize_order_number(order_number):
        """Привести номер заказа к единому формату (5 цифр) для сравнения."""
        match = re.search(r"\d+", str(order_number))
        if match:
            return match.group().zfill(5)
        return str(order_number).replace("#", "").strip().zfill(5)

    def wait_for_condition_or_false(self, condition, timeout=None):
        """Дождаться выполнения условия. Возвращает True, если условие выполнилось, иначе False."""
        try:
            self._get_wait(timeout).until(condition)
            return True
        except TimeoutException:
            return False