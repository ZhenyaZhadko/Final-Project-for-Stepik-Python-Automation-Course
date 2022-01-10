from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MAIN_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success .alertinner > strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")