from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button 'Add to basket' is not presented"
