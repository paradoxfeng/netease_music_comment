# -*- coding: utf-8 -*-

# Scrapy settings for music_comment project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music_comment'

SPIDER_MODULES = ['music_comment.spiders']
NEWSPIDER_MODULE = 'music_comment.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music_comment (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'http://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=5151c228a2fbc77b980eb8aadaf39c26,1517969449404; _ntes_nuid=5151c228a2fbc77b980eb8aadaf39c26; __utmz=94650624.1517969457.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); UM_distinctid=1617ba1b9ae832-09c097e0ca6585-5d4e211f-1fa400-1617ba1b9af5da; vjuids=6fb93d9a3.1617ba1c136.0.ae6a3756152c; P_INFO=tiancaiyujinfeng7@163.com|1523170884|2|cc|00&99|null&null&null#zhj&330100#10#0#0|&0||tiancaiyujinfeng7@163.com; __f_=1523524231688; WM_TID=eufXFQv3J98gMXqHemVNG5g7Go3WQrzi; Province=0571; City=0571; vjlast=1518197654.1524202398.21; NNSSPID=4f429750c4bb46ca89fbe8d4e856a55e; vinfo_n_f_l_n3=6ed56a530e5d9bc1.1.4.1518197653875.1521393748910.1524202460372; __utmc=94650624; __utma=94650624.1151711844.1517969457.1524325288.1524330869.14; JSESSIONID-WYYY=Wmlu3V2u2R3tQWxpB5XkNDHzX3HIPdnizK0kXCg19W0V6qojRI82k0v%2B7JF7IhWPJQui7PduaZ6I3agO%2BxmxAkQsivs%5CIpkw7G9JehB%2F%2BYpf4rUXuY%2FaYr%2FVvqhCt1mfgM2ZF%2F%2FditRRDScjlRnPma9aQVOhaDKyJmkPVRNSEYprujh1%3A1524333941838; __remember_me=true; MUSIC_U=d91dee0665a160d44e8793ea37f8926c8ae7d768b71739cd72a6906814873e01892da7aeced779ec098c584a70116b164922ed9102ac8cbccddbaee124c51eaf32db1626929b2c19; __csrf=4af4268292ca8d5656ad975793385745; __utmb=94650624.17.10.1524330869',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music_comment.middlewares.MusicCommentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music_comment.middlewares.MusicCommentDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'music_comment.pipelines.MongoPipeline': 300,
# }

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
MONGO_URI = 'localhost'
MONGO_DATABASE = 'music_comment'

DOWNLOADER_MIDDLEWARES_BASE = {

    'scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware': 1,

}