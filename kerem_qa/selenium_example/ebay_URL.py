from selenium.webdriver.common.by import By

from kerem_qa.selenium_example.seleniumBaseDalya import seleniumBaseDalya

base = seleniumBaseDalya()
driver = base.selenium_start()

driver.get("https://www.ebay.com/")
Advanced_text = driver.find_element(By.PARTIAL_LINK_TEXT,"Advanced").text

if (Advanced_text == "Advanced"):
    driver.find_element(By.PARTIAL_LINK_TEXT,"Advanced").click()
    print("test ok")
    url = driver.current_url
    print(url)
else:
    print("test failed")

driver.close()
