from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_alert_successful_registration(self):
        assert self.is_element_present(*MainPageLocators.ALERT_THX_FOR_REG),\
            "Not found alert with text Thanks for registering!"
