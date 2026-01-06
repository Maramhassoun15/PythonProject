import time
from selenium.webdriver import Keys
from kerem_qa.nike_final_project.globals import LOCATION_NAME
from kerem_qa.nike_final_project.nike_pages.locators import FindStoreLocators


class FindAStorePage:
    def __init__(self, driver):
        self.driver = driver

    def search_location_and_get_store_text(self):
        search_location = self.driver.find_element(*FindStoreLocators.SEARCH_LOCATION_AND_GET_TEXT)
        search_location.send_keys(LOCATION_NAME)
        search_location.send_keys(Keys.ENTER)
        time.sleep(3)
        store = self.driver.find_element(*FindStoreLocators.STORE)
        store_text = store.text
        return store_text



