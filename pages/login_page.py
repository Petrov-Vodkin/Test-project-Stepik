from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url does not contain the substring 'login'"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        browser = self.browser

        def push_keys(element, keys):
            browser.find_element(*element).send_keys(keys)
            return True

        assert (push_keys(LoginPageLocators.REG_EMAIL_FORM, email)), "Error while registering email"
        assert (push_keys(LoginPageLocators.REG_PASSWORD_FORM, password)), "Password registration error"
        assert (push_keys(LoginPageLocators.REG_CONFIRM_FORM, password)), "Password confirm registration error"
        browser.find_element(*LoginPageLocators.BUTTON_TO_REG).click()

    def should_not_be_reg_error_message(self):
        assert self.is_not_element_present(*LoginPageLocators.ERROR_MESSAGE), \
            "Error message is presented, but should not be"
