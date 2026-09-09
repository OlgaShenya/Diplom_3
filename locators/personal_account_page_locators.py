from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    """Локаторы для страницы личного кабинета"""
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
    QUIT = (By.XPATH, "//button[text()='Выход']")
    MY_LATEST_ORDER_NUMBER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]/li[1]//p[contains(@class, 'text_type_digits-default')]")
    ORDER_HISTORY_LIST = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]//li[contains(@class, 'OrderHistory_listItem')]")
    ORDER_HISTORY_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")
