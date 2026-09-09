import allure
from .base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountLocators
from url import Urls


class PersonalAccountPage(BasePage):
    """Page Object для страницы личного кабинета"""

    def __init__(self, driver, url=Urls.PERSONAL_ACCOUNT_PAGE_URL):
        super().__init__(driver, url)

    @allure.step("Кликнуть по разделу «Профиль»")
    def click_profile(self):
        """Кликнуть по разделу 'Профиль'"""
        profile_link = self.find_visible_element(PersonalAccountLocators.PROFILE_LINK)
        self.driver.execute_script("arguments[0].click();", profile_link)

    @allure.step("Проверить, что открыта страница профиля")
    def is_profile_page_opened(self):
        """Проверить, что открыта страница профиля (Личный кабинет)"""
        link = self.find_visible_element(PersonalAccountLocators.PROFILE_LINK)
        return link.get_attribute("aria-current") == "page"

    @allure.step("Кликнуть по разделу «История заказов»")
    def click_order_history(self):
        """Кликнуть по разделу 'История заказов'"""
        # Кликаем через JavaScript, чтобы обойти возможный overlay
        order_history_link = self.find_visible_element(PersonalAccountLocators.ORDER_HISTORY)
        self.driver.execute_script("arguments[0].click();", order_history_link)

    @allure.step("Проверить, что открыта страница истории заказов")
    def is_order_history_page_opened(self):
        """Проверить, что открыта страница истории заказов"""
        link = self.find_visible_element(PersonalAccountLocators.ORDER_HISTORY)
        return link.get_attribute("aria-current") == "page"

    @allure.step("Кликнуть по кнопке «Выход»")
    def click_quit_button(self):
        """Кликнуть по кнопке 'Выход'"""
        quit_btn = self.find_visible_element(PersonalAccountLocators.QUIT)
        self.driver.execute_script("arguments[0].click();", quit_btn)

    @allure.step("Получить номер последнего заказа из истории")
    def get_last_order_number(self):
        """Получить номер последнего (самого верхнего) заказа из истории"""
        order_element = self.find_visible_element(PersonalAccountLocators.MY_LATEST_ORDER_NUMBER)
        return order_element.text
