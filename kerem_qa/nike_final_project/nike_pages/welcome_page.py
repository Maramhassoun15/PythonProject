
from kerem_qa.nike_final_project.globals import HELP_BUTTON
from kerem_qa.nike_final_project.nike_pages.locators import WelcomeLocators


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver


    def click_on_women_button(self):
        women_button = self.driver.find_element(*WelcomeLocators.WOMEN_BUTTON)
        women_button.click()
    def click_on_men_button(self):
        men_button = self.driver.find_element(*WelcomeLocators.MEN_BUTTON)
        men_button.click()

    def click_on_Nike_Run_Club_button(self):
        run_club_button = self.driver.find_element(*WelcomeLocators.RUN_CLUB_BUTTON)
        run_club_button.click()
    def click_on_menu_button(self):
        menu_button = self.driver.find_element(*WelcomeLocators.MENU_BUTTON)
        menu_button.click()

    def verfiy_buttons_exist(self):
        new_button = self.driver.find_element(*WelcomeLocators.NEW_BUTTON).text
        assert new_button == 'New' ,"new button doesn't exist"

        men_button = self.driver.find_element(*WelcomeLocators.MEN_BUTTON).text
        assert men_button == 'Men' ,"men button doesn't exist"

        women_button = self.driver.find_element(*WelcomeLocators.WOMEN_BUTTON).text
        assert women_button == 'Women' ,"women button doesn't exist"

        kids_button = self.driver.find_element(*WelcomeLocators.KIDS_BUTTON).text
        assert kids_button == 'Kids' ,"kids button doesn't exist"

        sport_button = self.driver.find_element(*WelcomeLocators.SPORT_BUTTON).text
        assert sport_button == 'Sport' ,"sport button doesn't exist"

        sale_button = self.driver.find_element(*WelcomeLocators.SALE_BUTTON).text
        assert sale_button == 'Sale' ,"sale button doesn't exist"

    def click_on_find_a_store_button(self):
        findStore_button = self.driver.find_element(*WelcomeLocators.FINDSTORE_BUTTON)
        findStore_button.click()

    def click_on_Help_button(self):
        self.driver.get(HELP_BUTTON)



