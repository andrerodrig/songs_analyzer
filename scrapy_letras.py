import scrapy
import json

links = (link for link in json.load(open('data/external/links.json', 'r')))

class LyricsSpider(scrapy.Spider):
    name = 'LyricsScrapy'
    start_urls = [next(links)] 
    
    def parse(self, response):
        next_music = next(links)
        letra = response.xpath("*//div[@class='cnt-letra p402_premium']/p/text()").getall()
        if not letra:
            letra = response.xpath("*//div[@class='cnt-trad_r']/p/span/text()").getall()
        info = response.xpath("*//div[@class='breadcrumb cor_1 g-1']/span/a/span/text()").getall()
        try:
            title = info[3]
        except:
            title = response.xpath("*//div[@class='cnt-head_title']/h1/text()").getall() 
        yield {
            'title':title,
            'lyric': letra,
            'gender':info[1],
            'artist':info[2],
            }
        
    
        if next_music is not None:
            yield scrapy.Request(next_music, callback=self.parse)