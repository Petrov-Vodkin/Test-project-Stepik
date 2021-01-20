from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_btn_add_to_basket(self):
        btn_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        return btn_to_basket

    def check_product_name_in_alert(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text, "Invalid product name in alert"

