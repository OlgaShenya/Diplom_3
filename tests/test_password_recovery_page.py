import allure
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    """Тесты для страницы восстановления пароля"""
    
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    @allure.description("На странице входа кликаем «Восстановить пароль» и проверяем, что открылась страница восстановления пароля.")
    def test_go_to_password_recovery_page_from_login(self, driver):
        """
        Проверка перехода на страницу восстановления пароля 
        по кнопке «Восстановить пароль»
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password_button()
        
        recovery_page = PasswordRecoveryPage(driver)
        
        assert recovery_page.is_recovery_page_opened()
    
    
    @allure.title("Ввод email и клик по кнопке «Восстановить»")
    @allure.description("Вводим email на странице восстановления пароля и нажимаем «Восстановить».")
    def test_enter_email_and_click_recovery_button(self, driver, test_email):
        """
        Проверка ввода почты и клика по кнопке «Восстановить»
        """
        recovery_page = PasswordRecoveryPage(driver)
        recovery_page.open()
        recovery_page.enter_email(test_email)
        recovery_page.click_recovery_button()
        
        assert recovery_page.check_url("/forgot-password")