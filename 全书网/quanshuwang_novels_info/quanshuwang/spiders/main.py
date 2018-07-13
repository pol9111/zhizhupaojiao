# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quanshuwang.items import Info_Item

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['quanben.co']
    # 起始页是排行榜
    start_urls = ['http://www.quanben.co/top/allvisit_1.html',]

    # 爬取排行榜的每一页, 每一页的每本小说
    rules = (
        Rule(LinkExtractor(allow=r'allvisit_\d+')),
        Rule(LinkExtractor(allow=r'www.quanben.co/info/\d+.html'), callback='info_item'),
    )

    # 每一页的每一本小说详情页  点击阅读
    def info_item(self, response):
        item = Info_Item()

        item['info_title'] = response.xpath('//div[@id="content"]//h1/text()').extract()[0]
        item['author'] = response.xpath('//ul[@class="novel_msg"]/li[1]/a/text()').extract()[0]
        item['time'] = self.format_time(response)
        item['condition'] = response.xpath('//ul[@class="novel_msg"]/li[3]/em/text()').extract()[0]
        item['category'] = self.format_category(response)
        item['total_words'] = self.format_total_words(response)
        item['total_recommendations'] = response.xpath('//ul[@class="novel_msg"]/li[6]/em/text()').extract()[0]
        item['total_clicks'] = response.xpath('//div[@class="rank"]//p[@id="allGoldMedalOrder"]/text()').extract()[0]

        yield item

    def format_time(self, response):
        time = response.xpath('//ul[@class="novel_msg"]/li[2]/text()').extract()[0]
        return time.split('：')[1]

    def format_category(self, response):
        category = response.xpath('//ul[@class="novel_msg"]/li[4]/text()').extract()[0]
        return category.split('：')[1]

    def format_total_words(self, response):
        total_words = response.xpath('//ul[@class="novel_msg"]/li[5]/text()').extract()[0]
        return total_words.split('：')[1]






