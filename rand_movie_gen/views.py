from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from scrapyd_api import ScrapydAPI
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def index(request):
    settings = {
            'FEED_URI': 'result.json',
            'FEED_FORMAT': 'json'
        }
    task = scrapyd.schedule('default', 'top', settings=settings)
    print(task)
    return render(request, 'rand_movie_gen/index.html', {})




# from django.core.management.base import BaseCommand
# from scrape_top_movies.scrape_top_movies.spiders.scrape_movies import TopRatedMovies
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
#
# process = CrawlerProcess(get_project_settings())
#
# # var = name of spider
#
# process.crawl(TopRatedMovie)
# process.start()
