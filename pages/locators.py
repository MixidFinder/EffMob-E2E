from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_CONTAINER = (By.CSS_SELECTOR, "#login_button_container")
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login-button")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "#login_button_container > div > form > div.error-message-container.error > h3",
    )


class InventoryPageLocators:
    INVENTORY_CONTAINER = (By.CSS_SELECTOR, "#inventory_container")
    BACKPACK_ITEM_NAME = (By.CSS_SELECTOR, "#item_4_title_link > div")
    BACKPACK_IMAGE = (By.CSS_SELECTOR, "#item_4_img_link > img")
    BACKPACK_PRICE = (
        By.CSS_SELECTOR,
        "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div",
    )
    BACKPACK_ADD_TO_CART = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BACKPACK_REMOVE_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")


class ItemPageLocators:
    ITEM_CONTAINER = (By.CSS_SELECTOR, "#inventory_item_container")
    ITEM_NAME = (
        By.CSS_SELECTOR,
        "#inventory_item_container > div > div > div.inventory_details_desc_container > div.inventory_details_name.large_size",
    )
    ITEM_PRICE = (
        By.CSS_SELECTOR,
        "#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div",
    )
    ITEM_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "#add-to-cart")
    ITEM_REMOVE_BTN = (By.CSS_SELECTOR, "#remove")
    ITEM_IMAGE = (
        By.CSS_SELECTOR,
        "#inventory_item_container > div > div > div.inventory_details_img_container > img",
    )


class CartPageLocators:
    BACKPACK_CART_ITEM_NAME = (By.CSS_SELECTOR, "#item_4_title_link > div")
    BACKPACK_CART_REMOVE_BTN = (By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    BACKPACK_CART_PRICE = (
        By.CSS_SELECTOR,
        "#cart_contents_container > div > div.cart_list > div.cart_item > div.cart_item_label > div.item_pricebar > div",
    )
    CART_LIST = (By.CSS_SELECTOR, "#cart_contents_container > div > div.cart_list")
    CART_BACK_SHOPPING_BTN = (By.CSS_SELECTOR, "#continue-shopping")
    CART_CHECKOUT_BTN = (By.CSS_SELECTOR, "#checkout")


class CheckoutPageLocators:
    CHECKOUT_INFO = (
        By.CSS_SELECTOR,
        "#checkout_info_container > div > form > div.checkout_info",
    )
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE_INPUT = (By.CSS_SELECTOR, "#postal-code")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#continue")
    CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "#checkout_info_container > div > form > div.checkout_info > div.error-message-container.error > h3",
    )


class CheckoutTwoPageLocators:
    CHECKOUT_CONTAINER = (By.CSS_SELECTOR, "#checkout_summary_container")
    CHECKOUT_ITEM_PRICE = (
        By.XPATH,
        '//*[@id="checkout_summary_container"]/div/div[2]/div[6]/text()[2]',
    )
    CHECKOUT_TAX = (
        By.XPATH,
        '//*[@id="checkout_summary_container"]/div/div[2]/div[7]/text()[2]',
    )
    CHECKOUT_TOTAL = (
        By.XPATH,
        '//*[@id="checkout_summary_container"]/div/div[2]/div[8]/text()[2]',
    )
    CHECKOUT_CANCEL_BTN = (By.CSS_SELECTOR, "#cancel")
    CHECKOUT_FINISH_BTN = (By.CSS_SELECTOR, "#finish")


class CheckoutCompletePageLocators:
    COMPLETE_CONTAINER = (By.CSS_SELECTOR, "#checkout_complete_container")
    COMPLETE_HEADER = (By.CSS_SELECTOR, "#checkout_complete_container > h2")
    COMPLETE_BACK_BTN = (By.CSS_SELECTOR, "#back-to-products")


class BasePageLocators:
    CART_LINK = (By.CSS_SELECTOR, "#shopping_cart_container > a")
