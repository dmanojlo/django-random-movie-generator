import scrapy
import random
class TopRatedMovies(scrapy.Spider):

    name = 'top'

    start_urls = ['https://www.imdb.com/chart/top/']

    #custom_settings = { 'FEEDS': {'result.json': {'format': 'json'}}}

    def parse(self, response):
        a = random.randint(0,249)
        movie_name = response.css('.titleColumn a::text')[a].get()
        yield {'movie_name': movie_name}
