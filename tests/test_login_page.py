import allure
from pages.login_page import LoginPage


class TestLoginPage:
    """Тесты для страницы входа"""
    
    @allure.title("Кнопка показать/скрыть пароль подсвечивает поле ввода")
    @allure.description("На странице входа вводим пароль, кликаем по иконке показать/скрыть и проверяем, что поле пароля становится активным (подсвечивается).")
    def test_toggle_password_visibility_highlights_field(self, driver):
        """
        Проверка, что клик по кнопке показать/скрыть пароль 
        делает поле активным — подсвечивает его
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_password("test_password")
        login_page.click_toggle_password_visibility()
        assert login_page.is_password_field_highlighted()