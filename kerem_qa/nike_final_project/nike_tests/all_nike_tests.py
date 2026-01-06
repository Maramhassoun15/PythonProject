import time
import unittest
from kerem_qa.nike_final_project.globals import BASE_URL
from kerem_qa.nike_final_project.nike_pages.find_a_store_page import FindAStorePage
from kerem_qa.nike_final_project.nike_pages.help_page import HelpPage
from kerem_qa.nike_final_project.nike_pages.men_page import MenPage
from kerem_qa.nike_final_project.nike_pages.welcome_page import WelcomePage
from kerem_qa.nike_final_project.nike_pages.women_page import WomenPage
from kerem_qa.nike_final_project.seleniumBaseNaike import seleniumBaseNaike


class StartAllNikeTests(unittest.TestCase):
    def setUp(self):
        self.base = seleniumBaseNaike()
        self.driver = self.base.selenium_start_with_url(BASE_URL)
        self.welcome_page = WelcomePage(self.driver)
        self.women_page = WomenPage(self.driver)
        self.men_page = MenPage(self.driver)
        self.find_a_store_page = FindAStorePage(self.driver)
        self.help_page = HelpPage(self.driver)

    def tearDown(self):
        self.base.selenium_stop()


    def test_get_price_from_women_and_men(self):
        self.welcome_page.click_on_women_button()
        women_shirt_price = self.women_page.get_price_from_women()
        print(f"the price of the women shirt is:{women_shirt_price}")
        self.welcome_page.click_on_men_button()
        men_shirt_price = self.men_page.get_price_from_men()
        print(f"the price of the men shirt is:{men_shirt_price}")
        assert men_shirt_price > women_shirt_price, "women shirt price is greater than men shirt price"
        print(f"men shirt price is greater than women shirt price:{men_shirt_price}")

    def test_return_to_welcome_page(self):
        self.welcome_page.click_on_Nike_Run_Club_button()
        time.sleep(3)
        self.welcome_page.click_on_menu_button()
        url = self.driver.current_url
        assert url == 'https://www.nike.com/il/',"did not return to welcome page as expected"
        print("returned to welcome page successfully")

    def test_find_buttons(self):
        self.welcome_page.verfiy_buttons_exist()
        print("all the 6 buttons exist")

    def test_search_store(self):
        self.welcome_page.click_on_find_a_store_button()
        store = self.find_a_store_page.search_location_and_get_store_text()
        assert "Haifa" in store,"store not found"
        print("store found successfully")

    def test_get_help(self):
        self.welcome_page.click_on_Help_button()
        support_text = self.help_page.search_help()
        assert "Support" in support_text,"support not found"
        print("support found successfully")





