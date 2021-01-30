from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, ".basket-mini > span > a.btn")


class BasketPageLocators:
    ITEMS_TO_BUY = (By.CSS_SELECTOR, "#basket_formset")
    TEXT_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.alert-danger")
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    BUTTON_TO_REG = (By.CSS_SELECTOR, "#register_form > button.btn")
    REG_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_CONFIRM_FORM = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators:
    ALERT_THX_FOR_REG = (By.CSS_SELECTOR, "#messages > div.alert-success")


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    PRODUCT_NAME_ALERT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, " div.col-sm-6.product_main > p.price_color")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, " div.alert > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div.alert")
