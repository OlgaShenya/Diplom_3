import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage


class TestMainPage:
    """Тесты для главной страницы"""

    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Кликаем по ссылке «Конструктор» и проверяем, что открыта главная страница.")
    def test_click_constructor_link(self, driver):
        """Проверка перехода по клику на «Конструктор»"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.ensure_no_modal()
        main_page.click_constructor_link()

        assert main_page.is_main_page_opened()

    @allure.title("Переход по клику на «Лента Заказов»")
    @allure.description("Кликаем по ссылке «Лента Заказов» и проверяем, что открылась страница ленты заказов.")
    def test_click_feed_link(self, driver):
        """Проверка перехода по клику на «Лента заказов»"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_feed_link()

        feed_page = FeedPage(driver)
        feed_page.wait_for_page_load()
        assert feed_page.is_feed_page_opened()

    @allure.title("Клик по ингредиенту открывает модальное окно с деталями")
    @allure.description("Кликаем по ингредиенту и проверяем, что открылось модальное окно с деталями.")
    def test_click_ingredient_opens_modal(self, driver):
        """Проверка, что клик по ингредиенту открывает модальное окно"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()

        assert main_page.is_ingredient_modal_opened()

    @allure.title("Модальное окно ингредиента закрывается по клику на крестик")
    @allure.description("Открываем модальное окно ингредиента, закрываем его крестиком и проверяем, что окно закрылось.")
    def test_close_modal_by_cross(self, driver):
        """Проверка закрытия модального окна кликом по крестику"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_first_ingredient()

        main_page.close_ingredient_modal()

        assert not main_page.is_ingredient_modal_opened()

    @allure.title("Добавление ингредиента увеличивает его счётчик")
    @allure.description("Перетаскиваем ингредиент в заказ и проверяем, что его счётчик увеличился.")
    def test_add_ingredient_increases_counter(self, driver):
        """Проверка, что при добавлении ингредиента увеличивается счетчик"""
        main_page = MainPage(driver)
        main_page.open()

        initial_counter = main_page.get_first_ingredient_counter()

        main_page.add_first_ingredient_to_burger()

        new_counter = main_page.get_first_ingredient_counter()
        assert new_counter == initial_counter + 2

    @allure.title("Залогиненный пользователь может оформить заказ")
    @allure.description("Логинимся, добавляем ингредиент, оформляем заказ и проверяем, что появилось модальное окно успешного заказа.")
    def test_place_order(self, driver, test_email, test_password):
        """Проверка, что залогиненный пользователь может оформить заказ"""
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()

        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)

        main_page.wait_for_page_load()

        main_page.add_first_ingredient_to_burger()
        main_page.click_order_button()

        assert main_page.is_order_success_modal_opened()
