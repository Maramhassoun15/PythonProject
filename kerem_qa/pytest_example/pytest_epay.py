import time
import unittest

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

class pytest_epay(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.ebay.com/")

    def tearDown(self):
        self.base.selenium_stop()

    def test_advanced_button(self):
        print("test start")
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()
        URL = self.driver.current_url
        assert URL == "https://www.ebay.com/sch/ebayadvsearch" ,"URL have to be:https://www.ebay.com/sch/ebayadvsearch"
        print("advanced button have been clicked")

    def test_enter_button(self):
        item = "shirt"
        print("test start")
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()
        enter_button = self.driver.find_element(By.CLASS_NAME,"textbox__control")
        enter_button.send_keys(item)
        enter_button.send_keys(Keys.ENTER)
        url = self.driver.current_url
        assert item in url,"url should contain the word 'shirt'"
        print("item was find successfully")

    def test_Keyword_options(self):
        item = "shirt"
        print("test start")
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        enter_button = self.driver.find_element(By.CLASS_NAME,"textbox__control")
        enter_button.send_keys(item)

        keyword_options = Select(self.driver.find_element(By.ID,"s0-1-20-4[0]-7[1]-_in_kw"))
        keyword_options.select_by_index(2)
        print("keyword options was found successfully")

        enter_button.send_keys(Keys.ENTER)
        url = self.driver.current_url
        assert item in url, "url should contain the word 'shirt'"
        print("item was find successfully")

    def test_checkbox(self):
        advanced_button = self.driver.find_element(By.LINK_TEXT, "Advanced")
        advanced_button.click()

        check_box = self.driver.find_element(By.ID,"s0-1-20-5[1]-[1]-LH_Complete")
        self.base.click_and_assert_on_element(check_box)

        radio_button = self.driver.find_element(By.ID,"s0-1-20-6[4]-[0]-LH_ItemCondition")
        radio_button.click()

        print("radio button was clicked")













