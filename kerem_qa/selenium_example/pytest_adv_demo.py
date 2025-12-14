import time
import unittest

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

class pytest_swaglabs(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://advantageonlineshopping.com/#/")

    def tearDown(self):
        self.base.selenium_stop()


    def test_dropdown_example(self):
        print("test dropdown example")
        time.sleep(3)
        contact_us = self.driver.find_element(By.PARTIAL_LINK_TEXT,"CONTACT")
        contact_us.click()

        category = self.driver.find_element(By.NAME,"categoryListboxContactUs")
        category_as_dropdown = Select(category)
        category_as_dropdown.select_by_index(2)
        category_as_dropdown.select_by_visible_text("Mice")
        print("into category")

        time.sleep(3)
        product = Select(self.driver.find_element(By.NAME,"productListboxContactUs"))
        product.select_by_index(2)


        Email = self.driver.find_element(By.NAME,"emailContactUs")
        Email.send_keys("meme1234@gmail.com")


        supject = self.driver.find_element(By.NAME,"subjectTextareaContactUs")
        supject.send_keys("HI")

        send = self.driver.find_element(By.ID,"send_btn")
        is_displayd = send.is_displayed()
        assert is_displayd == True,("send button did not displayd")








