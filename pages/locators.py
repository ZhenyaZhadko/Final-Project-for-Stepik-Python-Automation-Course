from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    FULL_BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner p:nth-child(1) a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_KEY = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn-lg")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MAIN_PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > .alert-success .alertinner > strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")