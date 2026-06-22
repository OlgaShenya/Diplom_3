import allure
from .base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from url import Urls


class FeedPage(BasePage):
    """Page Object для страницы ленты заказов"""

    def __init__(self, driver, url=Urls.FEED_PAGE_URL):
        super().__init__(driver, url)

    @allure.step("Проверить, что открыта страница ленты заказов")
    def is_feed_page_opened(self):
        """Проверить, что открыта страница ленты заказов"""
        return self.is_element_visible(FeedPageLocators.FEED_PAGE_TITLE, timeout=10)

    @allure.step("Дождаться загрузки страницы ленты заказов")
    def wait_for_page_load(self):
        """Дождаться загрузки страницы ленты заказов"""
        self.find_visible_element(FeedPageLocators.FEED_PAGE_TITLE)

    @allure.step("Кликнуть по первому заказу в ленте")
    def click_first_order_in_feed(self):
        """Кликнуть по первому заказу в ленте"""
        order_link = self.find_clickable_element(FeedPageLocators.FEED_ORDER_ITEM_LINK)
        self.driver.execute_script("arguments[0].click();", order_link)

    @allure.step("Проверить, что открыта модалка заказа")
    def is_order_modal_opened(self):
        """Проверить, что открыта модалка заказа"""
        return self.is_element_visible(FeedPageLocators.ORDER_ITEM_MODAL, timeout=5)

    @allure.step("Закрыть модалку заказа")
    def close_order_modal(self):
        """Закрыть модалку заказа"""
        close_btn = self.find_clickable_element(FeedPageLocators.ORDER_MODAL_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click();", close_btn)
        self.wait_for_element_invisible(FeedPageLocators.ORDER_ITEM_MODAL)

    @allure.step("Получить значение счётчика «Выполнено за все время»")
    def get_total_orders_done(self):
        """Получить значение счётчика 'Выполнено за все время'"""
        counter_element = self.find_visible_element(FeedPageLocators.TOTAL_ORDERS_DONE)
        return int(counter_element.text)

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_today_orders_done(self):
        """Получить значение счётчика 'Выполнено за сегодня'"""
        counter_element = self.find_visible_element(FeedPageLocators.TODAY_ORDERS_DONE)
        return int(counter_element.text)

    @allure.step("Получить список номеров заказов в разделе «В работе»")
    def get_orders_in_work(self):
        """Получить список номеров заказов в разделе 'В работе'"""
        orders = self.driver.find_elements(*FeedPageLocators.ORDERS_IN_WORK_ITEM)
        return [self.normalize_order_number(order.text) for order in orders]

    @allure.step("Дождаться появления заказа в разделе «В работе»")
    def wait_for_order_in_work(self, order_number, timeout=30):
        """Дождаться появления номера заказа в разделе 'В работе'. Возвращает True/False."""
        clean_number = self.normalize_order_number(order_number)
        return self.wait_for_condition_or_false(
            lambda _: clean_number in self.get_orders_in_work(),
            timeout=timeout,
        )

    def _collect_visible_feed_numbers(self):
        """Собрать номера заказов из текущих элементов ленты"""
        numbers = set()
        for order in self.driver.find_elements(*FeedPageLocators.FEED_ORDER_ITEM):
            try:
                number_element = order.find_element(*FeedPageLocators.FEED_ORDER_NUMBER)
                numbers.add(self.normalize_order_number(number_element.text))
            except Exception:
                pass
        return numbers

    def _scroll_and_collect_feed_numbers(self):
        """Прокрутить ленту и собрать все видимые номера заказов"""
        feed_list = self.find_visible_element(FeedPageLocators.FEED_ORDER_LIST)
        all_numbers = set()
        previous_count = -1

        self.driver.execute_script("arguments[0].scrollTop = 0;", feed_list)

        while True:
            all_numbers.update(self._collect_visible_feed_numbers())
            if len(all_numbers) == previous_count:
                break
            previous_count = len(all_numbers)
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].clientHeight;",
                feed_list,
            )

        return all_numbers

    @allure.step("Проверить, что заказ есть в ленте")
    def is_order_in_feed(self, order_number, timeout=30):
        """Проверить, что номер заказа есть в ленте (с ожиданием появления)"""
        clean_number = self.normalize_order_number(order_number)
        return self.wait_for_condition_or_false(
            lambda _: clean_number in self._scroll_and_collect_feed_numbers(),
            timeout=timeout,
        )

    @allure.step("Дождаться появления всех заказов в ленте")
    def wait_for_orders_in_feed(self, order_numbers, timeout=60):
        """Дождаться появления всех номеров заказов в ленте. Возвращает True/False."""
        expected_numbers = {
            self.normalize_order_number(number) for number in order_numbers
        }
        return self.wait_for_condition_or_false(
            lambda _: expected_numbers.issubset(self._scroll_and_collect_feed_numbers()),
            timeout=timeout,
        )
