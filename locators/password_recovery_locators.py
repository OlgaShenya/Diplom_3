from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    """Локаторы для страницы восстановления пароля"""    
    PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
    PASSWORD_RECOVERY_INPUT = (By.XPATH, "//h2[text()='Восстановление пароля']/..//input")
    PASSWORD_RECOVERY_BTN = (By.XPATH, "//h2[text()='Восстановление пароля']/..//button")
