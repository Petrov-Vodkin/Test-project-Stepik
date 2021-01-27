from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_basket_page(self):
        link = self.browser.find_element(*MainPageLocators.BUTTON_VIEW_BASKET)
        link.click()

