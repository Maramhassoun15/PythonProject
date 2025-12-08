import time
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start()

driver.get("https://www.nike.com/il/")
driver.find_element(By.PARTIAL_LINK_TEXT,"Find").click()

url = driver.current_url
print(url)

if (url == "https://www.nike.com/il/retail"):
    print("Test OK -URL as expected")

else:
    print("Test FAILED -URL as expected")

driver.close()


