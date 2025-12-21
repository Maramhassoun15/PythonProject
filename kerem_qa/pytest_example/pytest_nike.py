import unittest

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from kerem_qa.coding_exec.string_exec import index_1
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class pytest_nike_price(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.nike.com/il/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_nike_shoes_price(self):
        search_field = self.driver.find_element(By.ID, "gn-search-input")
        search_field.click()
        search_field.send_keys("shoes")
        search_field.send_keys(Keys.ENTER)
        price_shoes = self.driver.find_elements(By.CLASS_NAME,"product-card__animation_wrapper")
        price_shoes_text = price_shoes[1].text
        index_1 = price_shoes_text.index("₪")+1
        price_shoes_text = price_shoes_text[index_1:]
        print(price_shoes_text)

        # assert price_shoes_text > 500, ""
        # print(price_shoes_text)




