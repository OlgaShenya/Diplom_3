import allure
import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage


class TestFeedPage:
    """Тесты для раздела 'Лента заказов'"""

    @allure.title("Клик по заказу в ленте открывает модальное окно с деталями")
    @allure.description("Открываем «Лента заказов», кликаем по первому заказу и проверяем, что открылось всплывающее окно с деталями.")
    def test_click_order_opens_modal(self, driver):
        """Проверка: если кликнуть на заказ, откроется всплывающее окно с деталями"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.ensure_no_modal()
        main_page.click_feed_link()
        feed_page = FeedPage(driver)
        feed_page.wait_for_page_load()
        feed_page.click_first_order_in_feed()

        assert feed_page.is_order_modal_opened(), "Модалка заказа не открылась"

    @allure.title("Созданный заказ пользователя отображается в общей ленте заказов")
    @allure.description("Логинимся, создаём новый заказ и проверяем, что его номер появляется на странице «Лента заказов».")
    def test_user_orders_appear_in_feed(self, driver, test_email, test_password):
        """
        Проверка: вновь созданный заказ пользователя из раздела «История заказов»
        отображается на странице «Лента заказов»
        """
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)
        main_page.wait_for_page_load()
        main_page.add_first_ingredient_to_burger()
        main_page.click_order_button()
        new_order_number = main_page.get_order_number()
        main_page.close_order_success_modal()
        main_page.click_feed_link()
        feed_page = FeedPage(driver)
        feed_page.wait_for_page_load()

        assert feed_page.is_order_in_feed(new_order_number), \
            f"Новый заказ {new_order_number} не отображается в ленте заказов"

    @allure.title("Создание заказа увеличивает счётчик «{counter_name}»")
    @allure.description("Запоминаем счётчик, создаём новый заказ и проверяем, что он увеличился.")
    @pytest.mark.parametrize(
        "counter_getter, counter_name",
        [
            ("get_total_orders_done", "Выполнено за всё время"),
            ("get_today_orders_done", "Выполнено за сегодня"),
        ],
        ids=["total", "today"],
    )
    def test_create_order_increases_counter(
        self, driver, test_email, test_password, counter_getter, counter_name
    ):
        """Проверка: при создании заказа счётчик выполненных заказов увеличивается"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)
        main_page.wait_for_page_load()
        main_page.click_feed_link()
        feed_page = FeedPage(driver)
        feed_page.wait_for_page_load()
        initial_counter = getattr(feed_page, counter_getter)()
        main_page.click_constructor_link()
        main_page.wait_for_page_load()
        main_page.add_first_ingredient_to_burger()
        main_page.click_order_button()
        main_page.close_order_success_modal()
        main_page.click_feed_link()
        feed_page.wait_for_page_load()
        new_counter = getattr(feed_page, counter_getter)()
        assert new_counter > initial_counter, \
            f"Счётчик '{counter_name}' не увеличился: было {initial_counter}, стало {new_counter}"

    @allure.title("Номер оформленного заказа появляется в разделе «В работе»")
    @allure.description("Оформляем заказ и проверяем, что его номер отображается в разделе «В работе» ленты заказов.")
    def test_order_number_appears_in_work_section(self, driver, test_email, test_password):
        """Проверка: после оформления заказа его номер появляется в разделе 'В работе'"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)
        main_page.wait_for_page_load()
        main_page.add_first_ingredient_to_burger()
        main_page.click_order_button()
        order_number = main_page.get_order_number()
        main_page.close_order_success_modal()
        main_page.click_feed_link()
        feed_page = FeedPage(driver)
        feed_page.wait_for_page_load()
        assert feed_page.wait_for_order_in_work(order_number), \
            f"Заказ {order_number} не появился в разделе 'В работе'"
