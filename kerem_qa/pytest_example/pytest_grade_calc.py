import unittest

from selenium.webdriver.common.by import By

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

class pytest_grade_calc(unittest.TestCase):

    def setUp(self):
        self.base = seleniumBaseDalya()
        self.driver = self.base.selenium_start_with_url("https://www.calculator.net/grade-calculator.html")

    def tearDown(self):
        self.base.selenium_stop()

    def test_grade_calculator_example(self):
        print("test start")
        Grade = self.driver.find_element(By.NAME,"s1")
        Grade.clear()
        Grade.send_keys("87")

        Grade2 = self.driver.find_element(By.NAME,"s2")
        Grade2.clear()
        Grade2.send_keys("81")

        Grade3 = self.driver.find_element(By.NAME,"s3")
        Grade3.clear()
        Grade3.send_keys("90")

        calculate_button = self.driver.find_element(By.NAME,"x")
        calculate_button.click()

        average_grade = self.driver.find_element(By.CSS_SELECTOR, "p[class='verybigtext']")
        text = average_grade.text
        index_1 = text.index(":")+1
        index_2 = text.index("(")
        text = text[index_1:index_2]
        text_as_float = float(text)
        is_pass = text_as_float >= 80
        assert is_pass ,"the final average is less than 80"

        print(f"the average grade is {text}")


