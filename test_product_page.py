# import time
import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize("num_promo", [i for i in range(9)])
def test_guest_can_add_product_to_basket(browser, num_promo):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num_promo}"
    page = ProductPage(browser, link)
    page.open()
    btn_to_basket = page.should_be_btn_add_to_basket()
    btn_to_basket.click()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_alert()
    page.check_product_price_in_basket()
#    time.sleep(2)
