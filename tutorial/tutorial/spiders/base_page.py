from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from seleniumrequests import Firefox
from settings import LONG


def set_up_browser():
    profile = webdriver.FirefoxProfile()
    profile.set_preference("dom.max_script_run_time", 600)
    profile.set_preference("webdriver.log.file", "/tmp/firefox_console")
    driver = Firefox(firefox_profile=profile)
    driver.set_window_size(1920, 1080)
    driver.implicitly_wait(LONG)
    return driver


class PageOperations(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_css(self, css, stop=True):
        try:
            return self.driver.find_element_by_css_selector(css)
        except WebDriverException as ex:
            if stop:
                raise ex

    def find_elements_by_css(self, css, stop=True):
        try:
            return self.driver.find_elements_by_css_selector(css)
        except WebDriverException as ex:
            if stop:
                raise ex

    @staticmethod
    def find_sub_element_by_css(css, element, stop=True):
        try:
            return element.find_element_by_css_selector(css)
        except WebDriverException as ex:
            if stop:
                raise ex

    @staticmethod
    def find_sub_elements_by_css(css, element, stop=True):
        try:
            return element.find_elements_by_css_selector(css)
        except WebDriverException as ex:
            if stop:
                raise ex