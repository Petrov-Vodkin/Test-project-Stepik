import time
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    btn_to_basket = page.should_be_btn_add_to_basket()
    btn_to_basket.click()
    page.solve_quiz_and_get_code()
    page.check_product_name_in_alert()
    time.sleep(2)
