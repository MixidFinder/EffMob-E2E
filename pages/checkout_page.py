from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    def should_be_chekcout_info(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.CHECKOUT_INFO
        ), "Checkout info not presented"

    def should_be_first_name_input(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.FIRST_NAME_INPUT
        ), "First name input not presented"

    def should_be_last_name_input(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.LAST_NAME_INPUT
        ), "Last name input not presented"

    def should_be_postal_code_input(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.POSTAL_CODE_INPUT
        ), "Last name input not presented"

    def should_be_continue_btn(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.CONTINUE_BTN
        ), "Continue btn not presented"

    def should_be_cancel_btn(self):
        assert self.browser.find_element(
            *CheckoutPageLocators.CANCEL_BTN
        ), "Cansel btn not presented"

    def filling_checkout_form(self, firs_tname, last_name, postal_code):
        firstname_input = self.browser.find_element(
            *CheckoutPageLocators.FIRST_NAME_INPUT
        )
        firstname_input.send_keys(firs_tname)
        lastname_input = self.browser.find_element(
            *CheckoutPageLocators.LAST_NAME_INPUT
        )
        lastname_input.send_keys(last_name)
        postalcode_input = self.browser.find_element(
            *CheckoutPageLocators.POSTAL_CODE_INPUT
        )
        postalcode_input.send_keys(postal_code)

    def should_not_be_error(self):
        assert self.is_not_element_present(
            *CheckoutPageLocators.ERROR_MESSAGE
        ), self.browser.find_element(*CheckoutPageLocators.ERROR_MESSAGE).text

    def cansel_click(self):
        cansel_btn = self.browser.find_element(*CheckoutPageLocators.CANCEL_BTN)
        cansel_btn.click()

    def continue_click(self):
        continue_btn = self.browser.find_element(*CheckoutPageLocators.CONTINUE_BTN)
        continue_btn.click()
