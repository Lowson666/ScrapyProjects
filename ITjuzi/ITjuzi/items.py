# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItjuziItem(scrapy.Item):
    #公司名称
    companyNAME = scrapy.Field()
    #投资状态
    companyROUND = scrapy.Field()
    #公司口号
    slogan = scrapy.Field()
    #公司网址
    companyURL = scrapy.Field()
    #公司标签
    companyTAG = scrapy.Field()
    #公司简介
    companyINFO = scrapy.Field()
    #公司团队信息
    companyMEMBER = scrapy.Field()

