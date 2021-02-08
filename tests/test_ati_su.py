# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#
import time

import pytest

from pages.atisu import MainPage


def test_check_transport_button(web_browser):
    """ Кнопка 'Транспорт' активна и происходит переход. """

    page = MainPage(web_browser)
    page.ATI_TRANSPORT.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://trucks.ati.su/'


def test_check_search_results(web_browser):
    """ Поля 'Откуда' и 'Куда' активны и появляются результаты поиска. """

    page = MainPage(web_browser)
    page.ATI_TRANSPORT.click()
    page.wait_page_loaded()
    page.ATI_FROM.send_keys('Беларусь')
    page.ATI_TO.send_keys('Россия')
    page.ATI_SEARCH_BUTTON.click()
    page.wait_page_loaded()

    assert page.ATI_SEARCH_RESULTS.is_presented()


@pytest.mark.skip(reason="In development")
def test_check_popup_registration(web_browser):
    """ При нажатии в карточке 'Показать контакты' появляется попап регистрации. """

    page = MainPage(web_browser)
    page.ATI_TRANSPORT.click()
    page.wait_page_loaded()
    page.ATI_FROM.send_keys('Беларусь')
    page.ATI_TO.send_keys('Россия')
    page.ATI_SEARCH_BUTTON.click()
    page.wait_page_loaded()
    page.ATI_AVAILABLE_CARS[-1].click()
    time.sleep(3)
    assert page.ATI_POPUP.is_visible()
