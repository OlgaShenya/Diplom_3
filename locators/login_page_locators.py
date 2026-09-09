from selenium.webdriver.common.by import By


class LoginPageLocators:
    """Локаторы для страницы входа"""
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
    FORGOT_PASSWORD_BTN = (By.XPATH, "//a[text()='Восстановить пароль']")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    TOGGLE_PASSWORD_VISIBILITY_ICON = (By.XPATH, "//input[@type='password']/following-sibling::div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT_CONTAINER = (By.XPATH, "//label[text()='Пароль']/..")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_BTN = (By.XPATH, "//button[text()='Войти']")