
from kerem_qa.nike_final_project.nike_pages.locators import WomenLocators


class WomenPage:
    def __init__(self, driver):
        self.driver = driver

    def get_price_from_women(self):
        clothing_button = self.driver.find_element(*WomenLocators.CLOTHING_BUTTON)
        clothing_button.click()
        price_shirt = self.driver.find_element(*WomenLocators.PRICE_SHIRT)
        price_shirt_text = price_shirt.text
        index = price_shirt_text.index("₪") + 1
        price_shirt_text = price_shirt_text[index:]
        return price_shirt_text
