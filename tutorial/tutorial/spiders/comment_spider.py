import scrapy
import csv
from selenium import webdriver
import time


class Common_Spider(scrapy.Spider):

    name = 'comment'
    start_urls = ['http://item.jd.com/4480572.html']

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url='http://item.jd.com/4480572.html')

    def _get_comment(self):
        item = self.driver.find_element_by_css_selector('.comment-item')
        comment_info = []
        for i in range(len(item)):
            user_name = self.driver.find_elements_by_css_selector('.comment-item .user-info').text
            user_level = self.driver.find_elements_by_css_selector('.comment-item .user-level').text
            user_comment = self.driver.find_elements_by_css_selector('.comment-item .comment-con').text
            order_info = self.driver.find_elements_by_css_selector('.comment-item .order-info').text
            comment_info.append({'user_name': user_name, 'user_level': user_level, 'user_comment': user_comment,
                                 'order_info': order_info})
        return comment_info

    def reach_comment_page(self):
        comment = self.driver.find_elements_by_css_selector('#detail .tab-main li')[4]
        comment.click()
        time.sleep(5)

    def get_csv(self):
        with open("comment.csv") as csvfile:
            filename = ['user_name', 'user_level', 'user_comment', 'order_info']
            write = csv.DictWriter(csvfile, fieldnames=filename)
            write.writeheader()
            write.writerow()
            csvfile.close()

    def parse(self, response):
        self.reach_comment_page()
        # self.driver.get(response.url)
        comment = []
        while True:
            comment_info = self._get_comment()
            comment += comment_info
            try:
                 next_page = self.driver.find_element_by_css_selector('.ui-pager-next')
                 if next_page:
                    next_page.click()
            except:
                break
        self.driver.close()

