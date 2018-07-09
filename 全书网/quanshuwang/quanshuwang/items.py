# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuanshuwangItem(scrapy.Item):
    # 存入信息的书名
    info_title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 类型
    category = scrapy.Field()
    # 目录
    catalog = scrapy.Field()
    # 书名 创建小说txt名, 并用于判断是否为该本小说的章节内容
    title = scrapy.Field()
    # 章节名
    chapter = scrapy.Field()
    # 每章内容
    content = scrapy.Field()


