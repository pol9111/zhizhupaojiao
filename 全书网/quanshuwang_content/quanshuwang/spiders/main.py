# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from quanshuwang.items import QuanshuwangItem

class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['quanben.co']
    # 起始页是排行榜
    start_urls = ['http://www.quanben.co/top/allvisit_1.html',]

    # 爬取排行榜的每一页, 每一页的每本小说
    rules = (
        Rule(LinkExtractor(allow=r'allvisit_\d+')),
        Rule(LinkExtractor(allow=r'www.quanben.co/info/\d+.html'), callback='info_item'),
        # Rule(LinkExtractor(allow=r'html/\d+/\d+/index.html'), callback='parse_item', follow=False),
    )

    # 每一页的每一本小说详情页  点击阅读
    def info_item(self, response):
        # item_info = QuanshuwangItem()
        # item_info['info_title'] = response.xpath('//div[@id="content"]//h1/text()').extract()[0]
        # item_info['author'] = response.xpath('//ul[@class="novel_msg"]/li[1]/a/text()').extract()[0]
        # item_info['category'] = response.xpath('//ul[@class="novel_msg"]/li[4]/text()').extract()[0]
        info = response.xpath('//li[@class="button2 white"]/a[1]/@href').extract()[0]
        url = 'http://www.quanben.co' + info
        yield scrapy.Request(url=url, callback=self.catalog_item)

    # 目录页
    def catalog_item(self, response):
        chapter_num = response.xpath('//li[@style="width:24%;"]/a/@href').extract()
        for num in chapter_num:
            pattern = re.compile(r'index.html')
            chapter_link = pattern.sub(num, response.url)
            yield scrapy.Request(url=chapter_link, callback=self.parse_item)

    # 小说主体内容
    def parse_item(self, response):
        item = QuanshuwangItem()
        item['title'] = response.xpath('//div[@class="z"]/a[4]/text()').extract()[0]
        item['chapter'] = response.xpath('//h1[@class="novel_title"]/text()').extract()[0]
        item['content'] = response.xpath('//div[@class="novel_content"]/text()').extract()
        yield item

