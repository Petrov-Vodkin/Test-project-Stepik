import time
import pytest
from pages.product_page import ProductPage


num = [i for i in range(10)]
num[7] = pytest.param("7", marks=pytest.mark.xfail)


@pytest.mark.parametrize("num_promo", [1, num[7]])
def test_guest_can_add_product_to_basket(browser, num_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    btn_to_basket = page.should_be_btn_add_to_basket()
    btn_to_basket.click()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_alert()
    page.check_product_price_in_basket()
    time.sleep(2)
    page.should_disappear()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    btn_to_basket = page.should_be_btn_add_to_basket()
    btn_to_basket.click()
    page.should_not_be_success_message()

