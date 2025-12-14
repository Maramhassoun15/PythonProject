import time
import unittest

from cffi.cffi_opcode import CLASS_NAME
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya


class pytest_calculator(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/interest-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_calculator_example(self):
        Initial_investment = self.driver.find_element(By.ID,"cstartingprinciple")
        Initial_investment.clear()
        Initial_investment.send_keys("200")
        Initial_investment.send_keys(Keys.ENTER)

        Annual_contribution = self.driver.find_element(By.ID, "cannualaddition")
        Annual_contribution.clear()
        Annual_contribution.send_keys("4000")
        Annual_contribution.send_keys(Keys.ENTER)

        radio_button = self.driver.find_elements(By.CLASS_NAME,"rbmark")
        radio_button[1].click()

        Compound = Select(self.driver.find_element(By.ID,"ccompound"))
        Compound.select_by_index(2)
        time.sleep(3)

        print_button = self.driver.find_element(By.LINK_TEXT,"Print")
        is_displayed = print_button.is_displayed()
        assert is_displayed == True,"print_button is not displayed"
