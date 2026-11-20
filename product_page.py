from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, product_name):
        # Находим сообщение об успехе
        messages = self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE)
        # Проверяем, что сообщение есть и оно ТОЧНО совпадает с названием товара
        assert messages, "Success message is not presented"
        assert messages[0].text == product_name, f"Expected name '{product_name}', but got '{messages[0].text}'"

    def should_be_correct_basket_total(self, product_price):
        # Находим сообщение со стоимостью корзины
        totals = self.browser.find_elements(*ProductPageLocators.BASKET_TOTAL_MESSAGE)
        # Проверяем, что сообщение есть и цена ТОЧНО совпадает
        assert totals, "Basket total message is not presented"
        assert totals[0].text == product_price, f"Expected price '{product_price}', but got '{totals[0].text}'"