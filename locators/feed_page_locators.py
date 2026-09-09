from selenium.webdriver.common.by import By


class FeedPageLocators:
    """Локаторы для страницы ленты заказов"""
    FEED_PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")

    ORDER_ITEM_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')][.//p[starts-with(text(), '#')]]")
    ORDER_MODAL_CLOSE_BTN = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]//button[contains(@class, 'Modal_modal__close')]")

    TOTAL_ORDERS_DONE = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')][preceding-sibling::p[contains(text(), 'Выполнено за все время')]]")
    TODAY_ORDERS_DONE = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')][preceding-sibling::p[contains(text(), 'Выполнено за сегодня')]]")

    FEED_ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    FEED_ORDER_ITEM = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//li[contains(@class, 'OrderHistory_listItem')]")
    FEED_ORDER_ITEM_LINK = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]//li[1]//a[contains(@class, 'OrderHistory_link')]")

    FEED_ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'text_type_digits-default')]")

    ORDERS_IN_WORK_ITEM = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li")
