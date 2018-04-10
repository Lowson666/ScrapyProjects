# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class DownlaodMmDouyuSpider(scrapy.Spider):
    name = 'downlaod-MM-douyu'
    allowed_domains = ['apiv2.douyucdn.cn']
    
    offset = 0
    url = "https://apiv2.douyucdn.cn/gv2api/rkc/roomlist/2_201/" 
    
    start_urls = [url + str(offset) + "/20/ios?client_sys=ios"]

    def parse(self, response):
        data = json.loads(response.text)["data"]["list"]
        for each in data:
            item = DouyuItem()
            item["nickname"] = each["nickname"]
            item["imagelink"] =each["vertical_src"]
           
            yield item
           
        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset) + "/20/ios?client_sys=ios", callback = self.parse)