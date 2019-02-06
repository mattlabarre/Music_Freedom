# -*- coding: utf-8 -*-
import scrapy


class TopchartsSpider(scrapy.Spider):
    name = 'topcharts'
    allowed_domains = ['www.at40.com']
    start_urls = ['https://www.at40.com/charts/top-40-238/latest/']

    def parse(self, response):
        #Pulls all of the containers that have the song and artist in them
        songs = response.xpath('//div[@class="chart-item-info"]/h3')
        for song in songs:
            #Pulls the individual songs from the containers
            title = song.xpath('./a/text()').extract_first()
            #Pulls the individual artists from the containers
            artist = song.xpath('.//small/a/text()').extract_first()

            #Used to output all of the songs and artists that are yielded
            yield {
                'Song':title,
                'Artist':artist,
            }
            
