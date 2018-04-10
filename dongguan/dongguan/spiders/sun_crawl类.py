# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://d.wz.sun0769.com/index.php/question/huiyin?page=0']

    rules = (
            Rule(LinkExtractor(allow=r'huiyin'),follow= True),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=False)
    )
    
    
    def parse_item(self, response):
      
        item = DongguanItem()
        item['number'] = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0].replace('\xa0','').split(':')[-1]
        item['url'] = response.url
        item['title'] = response.xpath("//div[@class='pagecenter p3']//strong/text()").extract()[0].replace('\xa0','').split('编号')[0]
        #由于网页保存含有图片文本和纯文字问不问的标签不同，所以需要在查找的时候判断是否为纯文本内容
        content = "".join(response.xpath("//div[@class='pagecenter p3']//div[@class='c1 text14_2']/text()").extract()).replace("\xa0","")
        #判断内容
        if content != "":
            #若不为空则为纯文本
            item['content'] = content
        else:
            #若为空则查找目标标签
            item['content'] ="".join(response.xpath("//div[@class='pagecenter p3']//div[@class='c1 text14_2']/div[@class='contentext']/text()").extract()).replace("\xa0","")
        
        
        yield item
        