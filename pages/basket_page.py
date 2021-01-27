from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items_to_buy(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Items presented in basket, but should not be"

    def should_be_text_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_IS_EMPTY), "Not found text - basket is empty"
