from selenium.webdriver.common.by import By


class FindStoreLocators(object):
    SEARCH_LOCATION_AND_GET_TEXT = (By.ID,"ta-Location_input")
    STORE = (By.CLASS_NAME,"d-sm-flx.mt1-sm")

class GetHelpLocators(object):
    HELP_FILD = (By.ID, "searchInput")
    SUPPORT = (By.PARTIAL_LINK_TEXT, "Support")

class MenLocators(object):
    CLOTHING_BUTTON = (By.LINK_TEXT, "Clothing")
    PRICE_SHIRT = (By.CLASS_NAME, "product-card__price")

class WomenLocators(object):
    CLOTHING_BUTTON = (By.LINK_TEXT, "Clothing")
    PRICE_SHIRT = (By.CLASS_NAME, "product-card__price")

class WelcomeLocators(object):
    WOMEN_BUTTON = (By.LINK_TEXT, "Women")
    MEN_BUTTON = (By.LINK_TEXT, "Men")
    RUN_CLUB_BUTTON = (By.LINK_TEXT, "Nike Run Club")
    MENU_BUTTON = (By.CLASS_NAME, "swoosh-svg")
    NEW_BUTTON = (By.LINK_TEXT, "New")
    KIDS_BUTTON = (By.LINK_TEXT, "Kids")
    SPORT_BUTTON = (By.LINK_TEXT, "Sport")
    SALE_BUTTON = (By.LINK_TEXT, "Sale")
    FINDSTORE_BUTTON = (By.CSS_SELECTOR,"[data-testid='desktop-user-menu-item-message-0']")


