# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
#from ITjuzi.items import ItjuziItem

class ItjzSpider(CrawlSpider):
    name = 'ITjz'
    allowed_domains = ['itjuzi.com']
    start_urls = ['http://www.itjuzi.com/company?page=1/']

    rules = [
        #Rule(link_extractor=LinkExtractor(allow=('/company\?page=\d+'))),
        Rule(LinkExtractor(allow=("page=\d+")), callback='parseITjuzi', follow=True)
        #Rule(LinkExtractor(allow=r'company/\d+'), callback='parse_item')
    ]

    def parseITjuzi(self, response):
        print(response.url)
        '''
        item = ItjuziItem()
        # 公司名称
        item['companyNAME'] = response.xpath('//div[@class="sec"]//h1/text()').extract()[0]
        # 投资状态
        item['companyROUND'] = response.xpath('//div[@class="sec"]//h1/span/text()').extract()[0]
        # 公司口号
        item['slogan'] = response.xpath('//div[@class="sec"]//div[@class="info-line"]/h2/text()').extract()[0]
        # 公司网址
        item['companyURL'] = response.xpath('//div[@class="sec"]//div[@class="link-line"]/a').extract()[0]
        # 公司标签
        item['companyTAG'] = ",".join(response.xpath('//div[@class="sec"]//div[@class="rowfoot"]/div[1]/div/a').extarct())
        # 公司简介
        item['companyINFO'] = response.xpath('//div[@class="thewrap"]/div[@class="boxed invest-info company-info company-new"]//div[@class="block"]/div/text()').extract()[0]

        yield item
'''
