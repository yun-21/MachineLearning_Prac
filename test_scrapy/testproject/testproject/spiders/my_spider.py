import scrapy

class FirstTest(scrapy.Spider):
    name = 'load'
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']

    def parse(self, response):
      for quote in response.css('div.MainPageBG.mp-box'):
        yield {
          'text': quote.css('h2.mp-h2::text').get(),
          }
