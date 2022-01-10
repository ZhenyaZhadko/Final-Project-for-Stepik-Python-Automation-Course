from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def alert_product_name_should_be_identical_to_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_NAME)
        alert_product_name = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_NAME)
        assert product_name.text == alert_product_name.text, "Product name is not the same"

    def alert_product_price_should_be_identical_to_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.MAIN_PRODUCT_PRICE)
        alert_product_price = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE)
        assert product_price.text == alert_product_price.text, "Product price is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear, but it didn't"