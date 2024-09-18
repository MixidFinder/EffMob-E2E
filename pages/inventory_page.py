from pages.base_page import BasePage
from pages.locators import InventoryPageLocators


class InventoryPage(BasePage):
    def test_add_to_cart(self):
        self.add_to_cart()
        self.should_be_remove_btn()

    def should_be_inventory_container(self):
        assert self.is_element_present(
            *InventoryPageLocators.INVENTORY_CONTAINER
        ), "Inventory container not presented"

    def add_to_cart(self):
        btn = self.browser.find_element(*InventoryPageLocators.BACKPACK_ADD_TO_CART)
        btn.click()

    def remove_from_cart(self):
        btn = self.browser.find_element(*InventoryPageLocators.BACKPACK_REMOVE_BTN)
        btn.click()

    def should_be_remove_btn(self):
        assert self.browser.find_element(
            *InventoryPageLocators.BACKPACK_REMOVE_BTN
        ), "Remove btn not presented"

    def should_be_add_btn(self):
        assert self.browser.find_element(
            *InventoryPageLocators.BACKPACK_ADD_TO_CART
        ), "Add to cart btn not presented"

    def get_item_name(self):
        return self.browser.find_element(*InventoryPageLocators.BACKPACK_ITEM_NAME).text