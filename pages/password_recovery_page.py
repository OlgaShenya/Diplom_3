import allure
from .base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from url import Urls


class PasswordRecoveryPage(BasePage):
    """Page Object для страницы восстановления пароля"""
    
    def __init__(self, driver, url=Urls.FORGOT_PASSWORD_PAGE_URL):
        super().__init__(driver, url)
    
    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_recovery_page_opened(self):
        """Проверить, что открыта страница восстановления пароля"""
        return self.is_element_visible(PasswordRecoveryLocators.PASSWORD_RECOVERY_TITLE)
    
    @allure.step("Ввести email для восстановления пароля")
    def enter_email(self, email):
        """Ввести email для восстановления пароля"""
        email_field = self.find_visible_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_INPUT)
        email_field.clear()
        email_field.send_keys(email)
        return self
    
    @allure.step("Нажать кнопку «Восстановить»")
    def click_recovery_button(self):
        """Нажать кнопку 'Восстановить'"""
        recovery_btn = self.find_clickable_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_BTN)
        recovery_btn.click()
        return self
    
    @allure.step("Получить значение поля email")
    def get_email_field_value(self):
        """Получить значение поля email"""
        email_field = self.find_visible_element(PasswordRecoveryLocators.PASSWORD_RECOVERY_INPUT)
        return email_field.get_attribute("value")
    
    @allure.step("Восстановить пароль (ввести email и нажать «Восстановить»)")
    def recovery_password(self, email):
        """Полный сценарий восстановления пароля"""
        self.enter_email(email)
        self.click_recovery_button()
        return self