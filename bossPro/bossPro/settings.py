# Scrapy settings for bossPro project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import random



BOT_NAME = 'bossPro'

SPIDER_MODULES = ['bossPro.spiders']
NEWSPIDER_MODULE = 'bossPro.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
LOG_LEVEL = 'ERROR'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    # 'Referer': 'https://www.zhipin.com/?ka=pc',
    # 'Cookie': "lastCity=101280600; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1666073105; wd_guid=5abdd3bc-f09b-4008-bdc4-6afbb0e86687; historyState=state; _bl_uid=tFlyg9mndwXs3gxqsj68m0Uhs48q; __zp_seo_uuid__=2227810d-bdef-44a6-af5b-680cb6e3983e; __g=-; __zp_stoken__=0a14edEx1GxF9ch9MJhEUYXAkZH1cfxMzUEwgRko3UwVYZG8Ib396D31hKwc/XFs8E29hWlcJXxhMPGJ0XgsGOwpvbGR2TQ8qUzFxC0pEYw4DXiEcZFhSCHNHIGJ9HH4Pbk51R18MFkAsaxNEWG1mSgsLUAFyFDYPC0MaCw97BQgMG3QyECsiVzFfRxY/JUwGHEQFZGBNDQ==; __l=r=https://www.baidu.com/link?url=BK-CjEX5ofTmyTWCqEdsixOoMs1EsWWqzNO-5h4Vx3Ss26dFn6STiRPcbaaASfi_&wd=&eqid=e5197bd900018d4900000006634e637d&l=/www.zhipin.com/web/geek/job?query=python&city=101280600&page=2&s=3&g=&friend_source=0&s=3&friend_source=0; __c=1666073105; __a=84328899.1666073105..1666073105.27.1.27.27; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1666081815",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bossPro.middlewares.BossproSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'bossPro.middlewares.BossproDownloaderMiddleware': 543,

}


# DOWNLOADER_CLIENTCONTEXTFACTORY = 'imgsPro.context.CustomContextFactory'
# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'bossPro.pipelines.MySQLPipline': 300,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# HTTPERROR_ALLOWED_CODES = [301,302]
# MEDIA_ALLOW_REDIRECTS =True
