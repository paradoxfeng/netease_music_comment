# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request,FormRequest
from netease_music_comment.items import MusicCommentItem
from urllib.parse import urlencode
import requests
import re
import json




class CommentSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['music.163.com/discover/artist']
    base_url = 'http://music.163.com'
    start_urls = ['http://music.163.com/discover/artist/cat?id=1001&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=1002&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=1003&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=2001&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=2002&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=2003&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=6001&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=6002&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=6003&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=7001&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=7002&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=7003&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=4001&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=4002&initial={initial}',
                  # 'http://music.163.com/discover/artist/cat?id=4003&initial={initial}'
                  ]

    def start_requests(self):
        for url in self.start_urls:
            for x in range(65,91):
                yield Request(url.format(initial=x),dont_filter=True)


    def parse(self, response):
        artists = response.xpath('//ul[@id="m-artist-box"]/li')
        for artist in artists:
            artist_name = artist.xpath('.//a[@class="nm nm-icn f-thide s-fc0"]/text()').extract_first()
            artist_id = artist.xpath('.//a[@class="nm nm-icn f-thide s-fc0"]/@href').extract_first()[11:].replace('=','')
            data = {'id': artist_id, 'limit': '200'}
            url = self.base_url + '/artist' + '/album?' + 'id=' + str(artist_id)
            yield Request(url,callback=self.parse_album,dont_filter=True)


    def parse_album(self,response):

        albums = response.xpath('//*[@id="m-song-module"]/li//a[@class="msk"]/@href').extract()
        if albums:
            print('存在')
        else:
            print('不存在')
        for album in albums:
            album_url = self.base_url + album
            yield Request(album_url,callback=self.parse_song,dont_filter=True)


    def parse_song(self,response):

        songs = response.xpath('//ul[@class="f-hide"]/li')
        for song in songs:
            song_id = song.xpath('./a/@href').extract_first()[9:]
            yield Request('http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(song_id),dont_filter=True,callback=self.parse_total_comment)
            try:
                res = requests.get('http://music.163.com/api/v1/resource/comments/R_SO_4_'+song_id,headers={
    'Cookie':'_iuqxldmzr_=32; _ntes_nnid=5151c228a2fbc77b980eb8aadaf39c26,1517969449404; _ntes_nuid=5151c228a2fbc77b980eb8aadaf39c26; __utmz=94650624.1517969457.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); UM_distinctid=1617ba1b9ae832-09c097e0ca6585-5d4e211f-1fa400-1617ba1b9af5da; vjuids=6fb93d9a3.1617ba1c136.0.ae6a3756152c; P_INFO=tiancaiyujinfeng7@163.com|1523170884|2|cc|00&99|null&null&null#zhj&330100#10#0#0|&0||tiancaiyujinfeng7@163.com; __f_=1523524231688; WM_TID=eufXFQv3J98gMXqHemVNG5g7Go3WQrzi; Province=0571; City=0571; vjlast=1518197654.1524202398.21; NNSSPID=4f429750c4bb46ca89fbe8d4e856a55e; vinfo_n_f_l_n3=6ed56a530e5d9bc1.1.4.1518197653875.1521393748910.1524202460372; __utmc=94650624; __utma=94650624.1151711844.1517969457.1524224863.1524235417.7; JSESSIONID-WYYY=45u7iNP7hdcF8C%2FlzUGBKlZ4Axdn0kTwtvmief%2BdBIuo7ZWJiyyUV%2Bx5JJjWDxc%2BnW2N5%2Fh7biFAj%5CzgZjh4sB3SmoUq4X1%2Bj99ITCXyCSbazh%5CAF7CHhRTIbbSFt9IyTBV%2BNukkOk9vZPsccU3wbhUWuvA25RihC7nOR4yGkgafZ7VK%3A1524239064031',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    })
                text = res.text
                result = json.loads(text)
                total = result['total']
                integer = int(total)//100
                for x in range(integer+2):
                    yield Request('http://music.163.com/api/v1/resource/comments/R_SO_4_'+str(song_id)+'?'+'limit=100&offset='+str(x*100),callback=self.parse_total_comment,dont_filter=True)
            except KeyError:
                return None


    def parse_total_comment(self,response):
        text = response.text
        result = json.loads(text)
        comments = result['comments']
        for comment in comments:
            item['comment'] = comment['content']
            yield item

