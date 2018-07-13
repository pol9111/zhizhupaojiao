# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from quanshuwang.settings import USER_AGENTS
from quanshuwang.settings import PROXIES


class RandomUserAgent(object):
    def process_request(self, request, spider):
        useragent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", useragent)


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            request.meta['proxy'] = "http://" + proxy["ip_port"]


