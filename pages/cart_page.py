from pages.base_page import BasePage
from pages.locators import CartPageLocators


class CartPage(BasePage):
    def should_be_cart_list(self):
        assert self.browser.find_element(
            *CartPageLocators.CART_LIST
        ), "Cart list not presented"

    def should_be_item_cart(self):
        assert self.browser.find_element(
            *CartPageLocators.BACKPACK_CART_ITEM_NAME
        ), "Backpack not presented"

    def should_be_remove_btn(self):
        assert self.browser.find_element(
            *CartPageLocators.BACKPACK_CART_REMOVE_BTN
        ), "Backpack remove btn not presented"

    def should_be_checkout_btn(self):
        assert self.browser.find_element(
            *CartPageLocators.CART_CHECKOUT_BTN
        ), "Checkout btn not presented"

    def should_be_back_btn(self):
        assert self.browser.find_element(
            *CartPageLocators.CART_BACK_SHOPPING_BTN
        ), "Back btn not presented"

    def remove_item(self):
        remove_btn = self.browser.find_element(
            *CartPageLocators.BACKPACK_CART_REMOVE_BTN
        )
        remove_btn.click()

    def checkout(self):
        checkout_btn = self.browser.find_element(*CartPageLocators.CART_CHECKOUT_BTN)
        checkout_btn.click()

    def should_not_be_item(self):
        assert self.is_not_element_present(
            *CartPageLocators.BACKPACK_CART_ITEM_NAME
        ), "Item is present but should not"
