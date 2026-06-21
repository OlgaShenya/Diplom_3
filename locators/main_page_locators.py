from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы для главной страницы"""
    PERSONAL_ACCOUNT_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAIN_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    FEED_LINK = (By.XPATH, "//a[.//p[text()='Лента Заказов']]")
    BURGER_INGREDIENT_ITEM_FIRST = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients__list')]/a[1]")
    BURGER_INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')][.//h2[text()='Детали ингредиента']]")
    BURGER_INGREDIENT_MODAL_CLOSE_BTN = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//button[contains(@class, 'Modal_modal__close')]")
    FIRST_BURGER_INGREDIENT_COUNTER = (By.XPATH, "//ul[contains(@class, 'BurgerIngredients_ingredients__list')]//a[1]//p[contains(@class, 'counter_counter__num')]")
    BURGER_CONSTRUCTOR_BUSKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')][.//p[contains(text(), 'идентификатор заказа')]]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//h2[contains(@class, 'text_type_digits-large')]")
    ORDER_SUCCESS_MODAL_CLOSE_BTN = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//button[contains(@class, 'Modal_modal__close')]")

    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE_CROSS = (By.XPATH, "//div[contains(@class, 'Modal_modal__close')]")