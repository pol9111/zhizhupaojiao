# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Info_Item(scrapy.Item):
    # 存入信息的书名
    info_title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 驻站时间
    time = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 状态
    condition = scrapy.Field()
    # 总字数
    total_words = scrapy.Field()
    # 总推荐
    total_recommendations = scrapy.Field()
    # 总点击数
    total_clicks = scrapy.Field()




