from pages.base_page import BasePage
from pages.locators import CheckoutCompletePageLocators


class CheckoutCompletePage(BasePage):
    def should_be_complete_container(self):
        assert self.browser.find_element(
            *CheckoutCompletePageLocators.COMPLETE_CONTAINER
        ), "Text not presented"

    def should_be_thank_text(self):
        assert self.browser.find_element(
            *CheckoutCompletePageLocators.COMPLETE_HEADER
        ), "Text not presented"

    def should_be_home_btn(self):
        assert self.browser.find_element(
            *CheckoutCompletePageLocators.COMPLETE_BACK_BTN
        )

    def home_click(self):
        home_btn = self.browser.find_element(
            *CheckoutCompletePageLocators.COMPLETE_BACK_BTN
        )
        home_btn.click()
