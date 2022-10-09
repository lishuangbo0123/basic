# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = "ERROR"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

FEED_EXPORT_ENCODING = 'utf-8'

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': r'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Referer': 'https://www.zhihu.com',
    'Connection': 'keep-alive',
    'Cookie':'_zap=8ff3179a-6702-40c4-9af4-a81ced542ed6; _xsrf=shbahvkvpCuf9544ZCJkEqmauPPpTnug; d_c0="ADDcxLyMxBKPTuSFm-b0MiwiIu2L0_kcUh8=|1615207876"; q_c1=a8524ea72b67417a86bb1fb6cff7ca83|1615208901000|1615208901000; _9755xjdesxxd_=32; YD00517437729195:WM_TID=Akfth/UgK/dABEQUERc73D99OuMay0ER; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1660801215,1663166346; captcha_session_v2=2|1:0|10:1663166346|18:captcha_session_v2|88:M3ZJMTlCRktZanRaTDh5MkNRSzBPV25NM1lPYVJyMjB2RFpLdHhRTDZtVVVpQjQxNkh5NHhnbUVkS2luYjAzNA==|7db547363c13a7d952bee5b230c4b577664e0452120850a64cc57b48a0b3a97d; __snaker__id=0vy0ehoSd3EQqtX5; gdxidpyhxdE=MbUWxHprCHj28Jf+2Td5IZ2Tu2wi/RLsBpZm/X8eEMYY7eehAbySvzYmGemj\mhW+zgi92ZxMgMbjB0b2nNnT2CogO24KNgjoVLaXzibzR//1eTB/bMggOsIMn960mzYY/7l6OsO2iAmclfuOnQ0Ye/7njZ2q/wCfJdqQhH2921dtBtt:1663167247650; YD00517437729195:WM_NI=ABp0VGp0ZvjvKsjFIW4Bw2e6bxAaH7CMkDUBuGwN1Rl9NJSUc+6Z9FqbYuiuyF8A2et630EwpMBD/l7B5fEdJwrAwcZYfePYuKD71wqOeG42+m9MjEFqX0lilpx3GoY5WVc=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eeaabc4db2988c93b646928e8bb7d45e829e8fadd849bcafa482eb4bb6b6a8b2fb2af0fea7c3b92a839ec0d1d54db4f09697e97e89ada6a7cc5df89eb9d3e83ea2a88f82cb3d8193a5a5d84ab799b9afb45ab0e782abd25fa1f5fabbbc4eb3be9796ec7fbb9af8a2b16fb8eafdd1c87db4938ea5ae68f59efb87c8708aa9bea2f6699a87aa86d353b7958cd8b47db391aba8b73ae9b3f7aee94f86af98d1ef63b0b0b8d4c6659beb99b7e237e2a3; z_c0=2|1:0|10:1663166371|4:z_c0|92:Mi4xb2JkQ0F3QUFBQUFBTU56RXZJekVFaVlBQUFCZ0FsVk5valVQWkFBWlIweGpHRExGR1VZOTNaNkwzdGtKSERSYXJR|2c4b709342fd8f835831671b060644f4225285be780032a35cdada46acca644e; SESSIONID=SV5xRsGma7bdeFO4ocDKBjDeCKykgbhb7BIiL518wTH; JOID=UlsRB0yvEvl0QXZ0CavmZGv__rQf_0PMDxQGNGTJJpwQJzc4Oojf2BNFcnMKsG2YkshwE_uLC2y6Rfba0vPvbvg=; osd=UlgdA0mvEfVwRHZ3Ba_jZGjz-rEf_E_IChQFOGDMJp8cIzI4OYTb3RNGfncPsG6Uls1wEPePDmy5SfLf0vDjav0=; BAIDU_SSP_lcr=https://www.baidu.com/link?url=P6WdqOphozibGuCt_S8-VOCxuhobJ3mFAw1cIXPNmc3&wd=&eqid=a6a1cc8100004422000000066322ca1e; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1663234209; NOT_UNREGISTER_WAITING=1; tst=r; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1663234726|1663224352',
}
HTTPERROR_ALLOWED_CODES = [401]
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html

ITEM_PIPELINES = {
   'zhihu.pipelines.ZhihuPipeline': 300,
    'zhihu.pipelines.MySQLPipline': 301,

    #300表示的是优先级，数值越小，优先级越高
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
