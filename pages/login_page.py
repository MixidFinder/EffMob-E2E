from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, username, password):
        username_input = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        username_input.send_keys(username)
        password_imput = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_imput.send_keys(password)
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.click()

    def should_not_be_login_error(self):
        assert self.is_not_element_present(
            *LoginPageLocators.ERROR_MESSAGE
        ), self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE).text

    def should_be_login_container(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_CONTAINER
        ), "Login container is not presented"
