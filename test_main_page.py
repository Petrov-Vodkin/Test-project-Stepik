# coding=utf-8

import pytest
import allure

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        self.page = MainPage(browser, link)
        self.page.open()

    @allure.feature('Main page')
    @allure.story('Гость может открыть страницу логина')
    @allure.severity('blocker')
    def test_guest_can_go_to_login_page(self, browser, setup):
        self.page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        with allure.step('Open login page'):
            allure.attach(browser.get_screenshot_as_png(), name='login_page_screen')

    @allure.feature('Main page')
    @allure.story('Гость может видеть ссылку логина')
    @allure.severity('critical')
    def test_guest_should_see_login_link(self, setup):
        self.page.should_be_login_link()


@allure.feature('Main page')
@allure.story('Гость может видеть продукт в корзине с главной страницы')
@allure.severity('trivial')
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_to_buy()
    basket_page.should_be_text_basket_is_empty()
