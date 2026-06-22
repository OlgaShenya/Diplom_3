import allure

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from url import Urls



class MainPage(BasePage):
    """Page Object для главной страницы"""
    
    def __init__(self, driver, url=Urls.MAIN_PAGE_URL):
        super().__init__(driver, url)
    
    @allure.step("Проверить, что открыта главная страница")
    def is_main_page_opened(self):
        """Проверить, что открыта главная страница"""
        return self.is_element_visible(MainPageLocators.MAIN_PAGE_TITLE)
    
    @allure.step("Нажать кнопку «Личный Кабинет» в хедере")
    def click_personal_account_button(self):
        """Нажать кнопку 'Личный Кабинет' в хедере"""
        personal_account_btn = self.find_clickable_element(MainPageLocators.PERSONAL_ACCOUNT_BTN)
        personal_account_btn.click()
    
    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_page_load(self):
        """Дождаться загрузки главной страницы"""
        self.find_visible_element(MainPageLocators.MAIN_PAGE_TITLE)
    
    @allure.step("Кликнуть по ссылке «Конструктор»")
    def click_constructor_link(self):
        """Кликнуть по ссылке 'Конструктор'"""
        link = self.find_clickable_element(MainPageLocators.CONSTRUCTOR_LINK)
        link.click()
    
    @allure.step("Кликнуть по ссылке «Лента Заказов»")
    def click_feed_link(self):
        """Кликнуть по ссылке 'Лента заказов'"""
        link = self.find_clickable_element(MainPageLocators.FEED_LINK)
        link.click()
    
    @allure.step("Кликнуть по первому ингредиенту")
    def click_first_ingredient(self):
        """Кликнуть по первому ингредиенту (откроет модалку)"""
        ingredient = self.find_clickable_element(MainPageLocators.BURGER_INGREDIENT_ITEM_FIRST)
        ingredient.click()
    
    @allure.step("Проверить, что открыто модальное окно ингредиента")
    def is_ingredient_modal_opened(self):
        """Проверить, что открыто модальное окно ингредиента"""
        return self.is_element_visible(MainPageLocators.BURGER_INGREDIENT_MODAL, timeout=2)
    
    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        """Закрыть модальное окно ингредиента"""
        close_btn = self.find_clickable_element(MainPageLocators.BURGER_INGREDIENT_MODAL_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click();", close_btn)
        self.wait_for_element_invisible(MainPageLocators.BURGER_INGREDIENT_MODAL)
    
    @allure.step("Получить значение счётчика первого ингредиента")
    def get_first_ingredient_counter(self):
        """Получить значение счетчика первого ингредиента"""
        counter_element = self.find_visible_element(MainPageLocators.FIRST_BURGER_INGREDIENT_COUNTER)
        return int(counter_element.text)
    
    @allure.step("Добавить первый ингредиент в бургер (drag-and-drop)")
    def add_first_ingredient_to_burger(self):
        """Перетащить первый ингредиент в корзину (drag-and-drop через JavaScript)"""
        ingredient = self.find_clickable_element(MainPageLocators.BURGER_INGREDIENT_ITEM_FIRST)
        basket = self.find_visible_element(MainPageLocators.BURGER_CONSTRUCTOR_BUSKET)
        
        self.driver.execute_script("""
            function simulateDragDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop'
                }

                function createCustomEvent(type) {
                    var event = new CustomEvent("Event")
                    event.initEvent(type, true, true)
                    event.dataTransfer = {
                        data: {},
                        setData: function(type, val) {
                            this.data[type] = val
                        },
                        getData: function(type) {
                            return this.data[type]
                        }
                    }
                    return event
                }

                var event = createCustomEvent(EVENT_TYPES.DRAG_START)
                sourceNode.dispatchEvent(event)

                var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
                dropEvent.dataTransfer = event.dataTransfer
                destinationNode.dispatchEvent(dropEvent)

                var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
                dragEndEvent.dataTransfer = event.dataTransfer
                sourceNode.dispatchEvent(dragEndEvent)
            }
            simulateDragDrop(arguments[0], arguments[1]);
        """, ingredient, basket)
    
    @allure.step("Нажать кнопку «Оформить заказ»")
    def click_order_button(self):
        """Нажать кнопку 'Оформить заказ'"""
        order_btn = self.find_clickable_element(MainPageLocators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].click();", order_btn)
    
    @allure.step("Проверить, что открыто модальное окно успешного заказа")
    def is_order_success_modal_opened(self):
        """Проверить, что открыто модальное окно успешного заказа"""
        return self.is_element_visible(MainPageLocators.ORDER_SUCCESS_MODAL)
    
    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        """Получить номер заказа из модального окна (ждёт, пока номер не изменится с 9999)"""
        order_number_element = self.find_visible_element(MainPageLocators.ORDER_NUMBER)
        self.wait.until(lambda driver: order_number_element.text != "9999")
        return order_number_element.text
    
    @allure.step("Закрыть модальное окно успешного заказа")
    def close_order_success_modal(self):
        """Закрыть модалку успешного заказа"""
        close_btn = self.find_clickable_element(MainPageLocators.ORDER_SUCCESS_MODAL_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click();", close_btn)
        self.wait_for_element_invisible(MainPageLocators.ORDER_SUCCESS_MODAL, timeout=2)

    @allure.step("Закрыть модальное окно, если оно открыто")
    def ensure_no_modal(self):
        """
        Закрывает модалку, если она открыта.
        Безопасно вызывать в начале любого теста.
        """
        if self.is_element_visible(MainPageLocators.MODAL_OVERLAY, 1):
            close_btn = self.find_clickable_element(MainPageLocators.MODAL_CLOSE_CROSS, timeout=2)
            close_btn.click()
            self.wait_for_element_invisible(MainPageLocators.MODAL_OVERLAY, 5)