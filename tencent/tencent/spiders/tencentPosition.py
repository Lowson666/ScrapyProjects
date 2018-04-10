# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem
    

class TencentpositionSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url = 'https://hr.tencent.com/position.php?&start='
    pageNum = 0 
    
    start_urls = [url + str(pageNum)]
    
    
    def parse(self, response):
        try:
            for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
                #初始化模型对象
                #职位名称
                item = TencentItem()
                item['positionName'] = each.xpath("./td[1]/a/text()").extract()[0]
                #详细链接
                item['positionLink'] = 'https://hr.tencent.com/' + each.xpath("./td[1]/a/@href").extract()[0]
                #职位类别
                item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
                #招聘人数
                item['positionNum'] = each.xpath("./td[3]/text()").extract()[0]
                #工作地点
                item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
                #发布时间
                item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
            
                yield item
        except IndexError:
            pass
           
        if self.pageNum < 1680 :
            self.pageNum += 10
        else:
            raise("检索完成")
     #每次处理完一页的数据后，重新发送下一页面的请求
        yield scrapy.Request(self.url + str(self.pageNum),callback = self.parse)
            
     