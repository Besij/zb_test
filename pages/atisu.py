from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://ati.su/'

        super().__init__(web_driver, url)

    ATI_TRANSPORT = WebElement(css_selector='a[data-name="link-transport"]')
    ATI_FROM = WebElement(css_selector='input[id="input-geo-from"]')
    ATI_TO = WebElement(css_selector='input[id="input-geo-to"]')
    ATI_SEARCH_BUTTON = WebElement(xpath='/html/body/div[2]/div[2]/main/div[2]/div[2]/div[2]/div[2]/div[1]/button')
    ATI_SEARCH_RESULTS = ManyWebElements(xpath='//div[@name="search-results"]')
    ATI_AVAILABLE_CARS = ManyWebElements(css_selector='button[icon="[object Object]"]')
    ATI_POPUP = WebElement(xpath='//*[contains(text(), "Вход в АТИ"]')
