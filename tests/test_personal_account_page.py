import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    """Тесты для страницы личного кабинета"""
    
    @allure.title("Переход в «Личный кабинет»")
    @allure.description("Логинимся и проверяем, что открывается страница профиля личного кабинета.")
    def test_go_to_personal_account_page(self, driver, test_email, test_password):
        """ Проверка перехода по клику на «Личный кабинет» """
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)
        main_page.wait_for_page_load()
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_profile()

        assert personal_account_page.is_profile_page_opened()


    @allure.title("Переход в раздел «История заказов»")
    @allure.description("Логинимся, открываем личный кабинет и переходим в раздел «История заказов».")
    def test_go_to_order_history(self, driver, test_email, test_password):
        """ Проверка перехода в раздел «История заказов» """
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_personal_account_button()
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)        
        main_page.click_personal_account_button()
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_order_history()

        assert personal_account_page.is_order_history_page_opened()


    @allure.title("Выход из аккаунта")
    @allure.description("Логинимся, выходим из аккаунта и проверяем, что открылась страница входа.")
    def test_logout_from_account(self, driver, test_email, test_password):
        """ Проверка выхода из аккаунта """
        main_page = MainPage(driver)
        main_page.open()
        main_page.ensure_no_modal()
        main_page.click_personal_account_button()
        
        login_page = LoginPage(driver)
        login_page.login(test_email, test_password)
        
        main_page.wait_for_page_load()
        main_page.click_personal_account_button()
        
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_quit_button()
        
        login_page_after_logout = LoginPage(driver)
        assert login_page_after_logout.is_login_page_opened()