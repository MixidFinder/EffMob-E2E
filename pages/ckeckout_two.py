from pages.base_page import BasePage
from pages.locators import CheckoutTwoPageLocators


class CheckoutTwoPage(BasePage):
    def should_be_checkout_container(self):
        assert self.browser.find_element(
            *CheckoutTwoPageLocators.CHECKOUT_CONTAINER
        ), "Checkout container not presented"

    def should_be_finish_btn(self):
        assert self.browser.find_element(
            *CheckoutTwoPageLocators.CHECKOUT_FINISH_BTN
        ), "Finish btn not presented"

    def should_be_cansel_btn(self):
        assert self.browser.find_element(
            *CheckoutTwoPageLocators.CHECKOUT_CANCEL_BTN
        ), "Cansel btn not presented"

    def finish_click(self):
        finish_btn = self.browser.find_element(
            *CheckoutTwoPageLocators.CHECKOUT_FINISH_BTN
        )
        finish_btn.click()

    def cansel_click(self):
        cansel_btn = self.browser.find_element(
            *CheckoutTwoPageLocators.CHECKOUT_CANCEL_BTN
        )
        cansel_btn.click()
