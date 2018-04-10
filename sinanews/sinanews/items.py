# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinanewsItem(scrapy.Item):
    #大标题
    parentTitle = scrapy.Field()
    #大标题的Url
    parentUrls = scrapy.Field()
    #小标题
    subTitle = scrapy.Field()
    #小标题的Url
    subUrls = scrapy.Field()
    # 小类目录存储路径
    subFilename = scrapy.Field()
    # 小类下的子链接
    sonUrls = scrapy.Field()
    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()

