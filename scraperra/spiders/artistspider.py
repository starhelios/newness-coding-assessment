from scrapy.exceptions import CloseSpider
import re
from datetime import datetime
import scrapy
import datetime
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from scraperra.items import ScraperraItem


var = 1
class StackoverflowSpider(scrapy.Spider):
    name = "pakwheelsp"
    page_num = 2
    # #start_urls = ['https://www.pakwheels.com/used-cars/']

    def start_requests(self):
        urls = [
            'https://www.pakwheels.com/used-cars/',
            'https://buy.carfirst.com/used-cars',
            'https://buy.carfirst.com/used-cars?page=2',
            'https://buy.carfirst.com/used-cars?page=3',
            'https://buy.carfirst.com/used-cars?page=4',
            'https://buy.carfirst.com/used-cars?page=5',
            'https://buy.carfirst.com/used-cars?page=6',
            'https://buy.carfirst.com/used-cars?page=7',
            'https://buy.carfirst.com/used-cars?page=8',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        items = ScraperraItem()
        global var
        if var==1:
            var=var+var

            car_name = response.css(".truncate a::text").extract()
            car_price = response.css(".generic-green").css("::text").extract()
            car_location = response.css(".generic-gray::text").extract()
            car_pic_link = response.css(".pic::attr(data-original)").extract()
            car_link = response.css(".nomargin ::attr(href)").extract()
            str = 'https://www.pakwheels.com'
            car_linkf = [str + x for x in car_link]


            for item in zip(car_name, car_price, car_location, car_pic_link, car_linkf):
                items = {'brand': item[0],
                         'price': item[1].strip().replace("PKR", '').replace(',', ''),
                         'location': item[2],
                         'pic': item[3],
                         'detail': item[4]}
                yield items

        else:
            car_name1 = response.css("h4::text").extract()
            car_price1 = response.css(".price").css("::text").extract()
            car_location1 = response.css("footer .text-muted::text").extract()
            car_pic_link1 = response.css(".lazyy::attr(src)").extract()
            car_link1 = response.css(".product_box ::attr(href)").extract()

            for item in zip(car_name1, car_price1, car_location1, car_pic_link1, car_link1):
                items = {'brand': item[0],
                'price':  item[1].strip().replace("PKR", '').replace(',', ''),
                'location':  item[2],
                'pic':  item[3],
                'detail': item[4]}
                yield items

                # next_page = 'https://buy.carfirst.com/used-cars?page={}'.format(self.page_num)
                # if self.page_num <= 8:
                #     self.page_num += 1
                #     self.start_requests(next_page)
                #     yield response.follow(next_page, callback=self.parse)


if __name__== '__main__':
    process = CrawlerProcess()
    process.crawl(StackoverflowSpider)
    process.start()