from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.ckeckout_complete import CheckoutCompletePage
from pages.ckeckout_two import CheckoutTwoPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestFull:
    def test_full(self, browser):
        url = "https://www.saucedemo.com/"
        page = LoginPage(browser)
        page.open(url)
        page.should_be_login_container()
        page.login_user("standard_user", "secret_sauce")
        page.should_not_be_login_error()
        page = InventoryPage(browser)
        page.should_be_cart_link()
        page.should_be_inventory_container()
        page.should_be_add_btn()
        page.add_to_cart()
        page.should_be_remove_btn()
        page.go_to_cart_page()
        page = CartPage(browser)
        page.should_be_cart_list()
        page.should_be_checkout_btn()
        page.should_be_back_btn()
        page.should_be_item_cart()
        page.should_be_remove_btn()
        page.checkout()
        page = CheckoutPage(browser)
        page.should_be_chekcout_info()
        page.should_be_first_name_input()
        page.should_be_last_name_input()
        page.should_be_postal_code_input()
        page.should_be_continue_btn()
        page.should_be_cancel_btn()
        page.filling_checkout_form("test", "test", "12345")
        page.should_not_be_error()
        page.continue_click()
        page = CheckoutTwoPage(browser)
        page.should_be_checkout_container()
        page.should_be_finish_btn()
        page.should_be_cansel_btn()
        page.finish_click()
        page = CheckoutCompletePage(browser)
        page.should_be_complete_container()
        page.should_be_thank_text()
        page.should_be_home_btn()
        page.home_click()
