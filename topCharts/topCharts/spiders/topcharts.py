# -*- coding: utf-8 -*-
import scrapy


class TopchartsSpider(scrapy.Spider):
    name = 'topcharts'
    allowed_domains = ['www.at40.com']
    start_urls = ['https://www.at40.com/charts/top-40-238/latest/']

    def parse(self, response):
        songs = response.xpath('//div[@class="chart-item-info"]/h3')
        for song in songs:
            title = song.xpath('./a/text()').extract_first()
            artist = song.xpath('.//small/a/text()').extract_first()

            yield {
                'Song':title,
                'Artist':artist,
            }
            
