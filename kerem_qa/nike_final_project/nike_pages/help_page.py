from selenium.webdriver import Keys
from kerem_qa.nike_final_project.globals import SUPPORT_TEXT
from kerem_qa.nike_final_project.nike_pages.locators import GetHelpLocators


class HelpPage:
    def __init__(self, driver):
        self.driver = driver

    def search_help(self,text_to_search=SUPPORT_TEXT):
        help_field = self.driver.find_element(*GetHelpLocators.HELP_FILD)
        help_field.send_keys(text_to_search)
        help_field.send_keys(Keys.ENTER)
        support = self.driver.find_element(*GetHelpLocators.SUPPORT)
        support_text =  support .text
        return  support_text

