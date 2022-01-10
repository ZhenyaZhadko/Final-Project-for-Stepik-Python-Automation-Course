from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasketPageLocators.FULL_BASKET_FORMSET), "Formset for full basket is presented on empty basket page"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_LINK), "Continue shopping link is not presented on empty basket page"
