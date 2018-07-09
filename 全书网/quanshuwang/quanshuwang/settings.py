# -*- coding: utf-8 -*-

# Scrapy settings for quanshuwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'quanshuwang'

SPIDER_MODULES = ['quanshuwang.spiders']
NEWSPIDER_MODULE = 'quanshuwang.spiders'


USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
]

PROXIES = [
        {"ip_prot" :"122.7.228.214:8080", "user_passwd" : ""},
        {"ip_prot" :"27.184.124.33:8118", "user_passwd" : ""},
        {"ip_prot" :"111.155.116.247:8123", "user_passwd" : ""},
        {"ip_prot" :"180.118.241.41:808", "user_passwd" : ""},
        {"ip_prot" :"221.228.17.172:8181", "user_passwd" : ""},
        {"ip_prot" :"125.121.112.113:6666", "user_passwd" : ""},
        {"ip_prot" :"122.246.52.26:8010", "user_passwd" : ""},
        {"ip_prot" :"111.155.116.247:8123", "user_passwd" : ""},
        {"ip_prot" :"122.114.31.177:808", "user_passwd" : ""},
        {"ip_prot" :"118.190.95.35:9001", "user_passwd" : ""},

]
# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# # 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# # 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 使用队列形式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# # 允许暂停，redis请求记录不丢失
# SCHEDULER_PERSIST = True
#
# REDIS_HOST = "192.168.1.8"
# REDIS_PORT = 6379



# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'quanshuwang.middlewares.QuanshuwangSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'quanshuwang.middlewares.RandomUserAgent': 100,
   'quanshuwang.middlewares.RandomProxy': 200,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'quanshuwang.pipelines.QuanshuwangPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline': 900,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
