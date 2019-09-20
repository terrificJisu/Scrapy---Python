# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    name = 'book_crawl'
    allowed_domains = ['hanbit.co.kr']

    start_urls = ['http://hanbit.co.kr/store/books/category_list.html?cate_cd=001',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=002',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=003',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=004',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=005',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=006',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=007',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=008',]

    rules = (
        Rule(LinkExtractor(allow=r'store/books/look.php\?p_code=.*'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'store/books/category_list\.html\?page=\d+&cate_cd=00\d+&str=p_pub_date'))
    )

    def parse_item(self, response):
        i = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()

        i['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()
        i['book_author'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="저자 : "]/span/text()').extract()
        i['book_translator'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="번역 : "]/span/text()').extract()
        i['book_pub_date'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="출간 : "]/span/text()').extract()
        i['book_isbn'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[strong/text()="ISBN : "]/span/text()').extract()
      
        return i 
