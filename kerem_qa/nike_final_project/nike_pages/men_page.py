
from kerem_qa.nike_final_project.nike_pages.locators import MenLocators


class MenPage:
    def __init__(self, driver):
        self.driver = driver


    def get_price_from_men(self):
        clothing_button = self.driver.find_element(*MenLocators.CLOTHING_BUTTON)
        clothing_button.click()
        price_shirt = self.driver.find_element(*MenLocators.PRICE_SHIRT)
        price_shirt_text = price_shirt.text
        index = price_shirt_text.index("₪") + 1
        price_shirt_text = price_shirt_text[index:7]
        return price_shirt_text
