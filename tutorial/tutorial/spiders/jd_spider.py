#coding: utf-8
import scrapy
import csv
from selenium.webdriver.common.by import By
from tutorial.settings import ICON, PHONE_NAME
from selenium import webdriver

reload(__import__('sys')).setdefaultencoding('utf-8')


class JdSpider(scrapy.Spider):
    name = "jd_phone"
    allowed_domains = ['jd.com']
    start_urls = ['http://search.jd.com/Search?keyword=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&'
                  'enc=utf-8&wq=%E4%B8%89%E6%98%9F%E6%89%8B%E6%9C%BA&pvid=56ad82a62c574addafc37fc636c8a7db']

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.jd.com/')
        self._reach_phone_page()

    def find_sub_element_by_css(self, selector, elem):
        return elem.find_element(By.CSS_SELECTOR, selector)

    def _reach_phone_page(self):
        search_elem = self.driver.find_element_by_css_selector('.form')
        self.find_sub_element_by_css('#key', search_elem).send_keys(PHONE_NAME.decode('utf-8'))
        button_elem = self.find_sub_element_by_css('.button', search_elem)
        button_elem.click()

    def _get_phone_info(self):
        item_element = self.driver.find_elements_by_css_selector(".goods-list-v2 .gl-i-wrap")
        item_length = len(item_element)
        phone_info = []
        for i in range(item_length):
            phone_price = self.find_sub_element_by_css(".p-price", item_element[i]).text
            phone_name = self.find_sub_element_by_css(".p-name em", item_element[i]).text
            try:
                if self.find_sub_element_by_css(".goods-icons-img", item_element[i]):
                    phone_name = "{}{}".format(ICON, phone_name)
            except:
                pass
            print "========================="
            print phone_name, phone_price
            print "=========================="
            phone_info.append({"Model name": phone_name, "Pricing": phone_price})
        return phone_info

    def csv_export(self, phone_info):
        with open('result.csv', 'w') as csvfile:
            field_names = ['Model name', 'Pricing']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(phone_info)
            csvfile.close()

    def parse(self, response):
        self.driver.get(response.url)
        info = []
        while True:
            phone_info = self._get_phone_info()
            info += phone_info
            self.csv_export(info)
            try:
                next_page = self.driver.find_element_by_css_selector(".pn-next")
                if next_page:
                    next_page.click()
                    # self.driver.implicitly_wait(1)
            except:
                break
        self.driver.close()