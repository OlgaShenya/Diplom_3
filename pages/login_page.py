import allure
from .base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from url import Urls


class LoginPage(BasePage):
    """Page Object для страницы входа"""
    def __init__(self, driver, url=Urls.LOGIN_PAGE_URL):
        super().__init__(driver, url)

    @allure.step("Проверить, что открыта страница входа")
    def is_login_page_opened(self):
        """Проверить, что открыта страница входа"""
        return self.is_element_visible(LoginPageLocators.LOGIN_TITLE)

    @allure.step("Нажать кнопку «Восстановить пароль»")
    def click_forgot_password_button(self):
        """Нажать кнопку 'Восстановить пароль'"""
        forgot_pwd_btn = self.find_clickable_element(LoginPageLocators.FORGOT_PASSWORD_BTN)
        self.driver.execute_script("arguments[0].click();", forgot_pwd_btn)

    @allure.step("Ввести email")
    def enter_email(self, email):
        """Ввести email"""
        email_field = self.find_visible_element(LoginPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """Ввести пароль"""
        password_field = self.find_visible_element(LoginPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    @allure.step("Нажать кнопку «Войти»")
    def click_login_button(self):
        """Нажать кнопку 'Войти'"""
        login_btn = self.find_clickable_element(LoginPageLocators.LOGIN_BTN)
        login_btn.click()

    @allure.step("Войти в аккаунт")
    def login(self, email, password):
        """Полный сценарий входа в аккаунт"""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.wait.until(lambda driver: "/login" not in driver.current_url)

    @allure.step("Нажать кнопку показать/скрыть пароль")
    def click_toggle_password_visibility(self):
        """Нажать кнопку показать/скрыть пароль (иконка глазика)"""
        toggle_icon = self.find_clickable_element(LoginPageLocators.TOGGLE_PASSWORD_VISIBILITY_ICON)
        toggle_icon.click()

    @allure.step("Проверить, что поле пароля подсвечено (активно)")
    def is_password_field_highlighted(self):
        """
        Проверить, подсвечено ли поле пароля после клика на show/hide.
        Подсветка реализуется добавлением класса 'input_status_active'
        к родительскому div поля пароля.
        """
        container = self.find_visible_element(LoginPageLocators.PASSWORD_INPUT_CONTAINER)
        container_classes = container.get_attribute("class")
        return "input_status_active" in container_classes