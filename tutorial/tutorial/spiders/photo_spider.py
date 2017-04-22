import scrapy
from selenium import webdriver
from selenium.webdriver.common.by import By

class photo_spider(scrapy.Spider):
    name = "jd_photo"
    allowed_domains = ['jd.com']
    start_urls = ['http://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_15127&sort=sort_rank_asc'
                  '&trans=1&JL=3_%E5%93%81%E7%89%8C_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89#J_crumbsBar']

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url='http://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_15127&sort=sort_rank_asc'
                  '&trans=1&JL=3_%E5%93%81%E7%89%8C_%E4%B8%89%E6%98%9F%EF%BC%88SAMSUNG%EF%BC%89#J_crumbsBar')

    def find_sub_element_by_css(self, elem, seletor):
        return elem.find_element(By.CSS_SELECTOR, seletor)

    def _get_photo(self):
        item_elem = self.driver.find_element_by_css_selector('.gl-warp .gl-i-wrap')
        photo = self.driver.find_element_by_css_selector('.p-img', item_elem)
        photo = self.driver.find_element_by_xpath()
    #
    # def parse(self, response):
