# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'
#HTTPERROR_ALLOWED_CODES = [404]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

COOKIE = {'d_c0': ' "AHDgwUhh5wyPTsFu2-f-ojQ_sYxdQ1FIblU', '_xsrf': ' 6a110cbb-2dab-4a9a-8c68-6ae8c65a47bc', 'q_c1': ' 0fa75ec65e0142dd95de33b784daad5f|1514466080000|1514466080000', '_zap': ' 55940724-d9a6-487c-84d0-499d326d09db', 'capsion_ticket': ' "2|1:0|10:1514466383|14:capsion_ticket|44:YjE3MjY4NThkNDQwNDYzZWE2ZGFmMjg5MDI2ZWYyY2U', 'l_n_c': '1', 'l_cap_id': '"MjFlMDhhNWQ5OTAzNGNmMmE2MDhhNmYyZGM0Y2Q0NjI', 'r_cap_id': '"Y2E0YWUwZWM2OTliNGZmYWIyMjFkMWZiZGI1YjZkZmU', 'cap_id': '"YjQ5ZGY3YmIzODFlNDM3MmI4NWYwNTcwMzVlNzk3OTM', 'n_c': '1', 'z_c0': '"2|1:0|10:1514466407|4:z_c0|92:Mi4xRW8zYkFRQUFBQUFBY09EQlNHSG5EQ1lBQUFCZ0FsVk5aem95V3dCVDdEOThqUEFBcjd6VDFIUmxXdXR5dkRhZXdn|1309fe62a2f1e0802237be2c080cdd2d1dc83813f47aadf53803db3c76e734f0"', '__utma': '155987696.1277793656.1514467344.1514467344.1514467344.1', '__utmc': '155987696', '__utmz': '155987696.1514467344.1.1.utmcsr'}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED =True
#COOKIES = 'd_c0 = "AHDgwUhh5wyPTsFu2-f-ojQ_sYxdQ1FIblU=|1514466080";_xsrf = 6a110cbb-2dab-4a9a-8c68-6ae8c65a47bc;q_c1 = 0fa75ec65e0142dd95de33b784daad5f|1514466080000|1514466080000;_zap = 55940724-d9a6-487c-84d0-499d326d09db;capsion_ticket = "2|1:0|10:1514466383|14:capsion_ticket|44:YjE3MjY4NThkNDQwNDYzZWE2ZGFmMjg5MDI2ZWYyY2U=|8ecb56a6137ddc0610d1ecc36754f9eaaa13ba265ec1059874a5ff2cee13bee2";l_n_c=1;l_cap_id="MjFlMDhhNWQ5OTAzNGNmMmE2MDhhNmYyZGM0Y2Q0NjI=|1514466255|f2fa785d05459d3f63119b81dad7d0bed7497907";r_cap_id="Y2E0YWUwZWM2OTliNGZmYWIyMjFkMWZiZGI1YjZkZmU=|1514466255|a198403de125f8de644fde19aaeb930db1fb803c";cap_id="YjQ5ZGY3YmIzODFlNDM3MmI4NWYwNTcwMzVlNzk3OTM=|1514466255|2f39cad65cedde83b8eb8693e8b0565970fc7b7d";n_c=1;z_c0="2|1:0|10:1514466407|4:z_c0|92:Mi4xRW8zYkFRQUFBQUFBY09EQlNHSG5EQ1lBQUFCZ0FsVk5aem95V3dCVDdEOThqUEFBcjd6VDFIUmxXdXR5dkRhZXdn|1309fe62a2f1e0802237be2c080cdd2d1dc83813f47aadf53803db3c76e734f0";__utma=155987696.1277793656.1514467344.1514467344.1514467344.1;__utmc=155987696;__utmz=155987696.1514467344.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/57.0',
'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihuuser.pipelines.MongoPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MONGO_URI = 'localhost:27017'
MONGO_DATABASE = 'test'