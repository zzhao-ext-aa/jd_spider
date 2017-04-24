#coding: utf-8
import scrapy
import csv
from spiders.base_page import set_up_browser, PageOperations
from phone_info import PhoneInfo
from settings import JD


class JdSpider(scrapy.Spider):
    name = "jd_phone"
    allowed_domains = ['jd.com']
    start_urls = [
        'https://list.jd.com/list.html?cat=9987,653,655'
        ]
    phone_info_list = []

    def __init__(self):
        self.driver = set_up_browser()
        self.operations = PageOperations(self.driver)

    def _get_phone_info(self):
        container_element = self.operations.find_element_by_css('.goods-list-v2')
        item_elements = self.operations.find_sub_elements_by_css(".gl-i-wrap", container_element, stop=False)
        for item_element in item_elements:
            phone_info = PhoneInfo()
            phone_info.price = self.operations.find_sub_element_by_css(".p-price strong", item_element).text
            phone_info.model = self.operations.find_sub_element_by_css(".p-name em", item_element).text
            phone_info.jd_icon = self._get_jd_icon(item_element)
            self.phone_info_list.append(phone_info)

    def _get_jd_icon(self, item_element):
        have_jd_icon = False
        jd_icon = self.operations.find_sub_element_by_css(".p-icons img", item_element, stop=False)
        if jd_icon:
            jd_icon_text = jd_icon.get_attribute("data-tips")
            if jd_icon_text in JD:
                have_jd_icon = True
        else:
            have_jd_icon = False
        return have_jd_icon

    def _compose_result(self):
        result = []
        for phone_info in self.phone_info_list:
            result_item = {}
            icon = "*" if phone_info.jd_icon else " "
            result_item["Model name"] = u"{}{}".format(phone_info.model, icon)
            result_item["Pricing"] = phone_info.price
            result.append(result_item)
        return result

    def write_to_csv(self):
        result = self._compose_result()
        with open('result_phone.csv', 'w') as csvfile:
            csvfile.write(u'\ufeff'.encode('utf8'))
            field_names = ['Model name', 'Pricing']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for item in result:
                writer.writerow({k: v.encode('utf8') for k, v in item.items()})
            csvfile.close()

    def parse(self, response):
        self.driver.get(response.url)
        self.operations.find_element_by_css('.s-brand a[title*="SAMSUNG"]').click()
        while True:
            self._get_phone_info()
            next_page = self.operations.find_element_by_css(".pn-next", stop=False)
            if not next_page:
                break
            next_page.click()
        self.write_to_csv()
        self.driver.close()