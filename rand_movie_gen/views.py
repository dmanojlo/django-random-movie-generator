from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from scrapyd_api import ScrapydAPI
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
# Create your views here.

#scrapyd = ScrapydAPI('http://localhost:6800')
scrapyd = ScrapydAPI('http://randmovie-scraper.herokuapp.com/')

@csrf_exempt
@require_http_methods(['POST', 'GET'])  # only get and post
def index(request):
    data = dict()
    # settings = {
    #         'FEED_URI': 'result.json',
    #         'FEED_FORMAT': 'json'
    #     }
    task = ''
    if request.method == 'POST':
    # task_id = request.GET.get('task_id', None)
    # print(task_id)
    # if task_id is None:
        task = scrapyd.schedule('default', 'top')
        return JsonResponse({'task':task})
    elif request.method == 'GET':
        task_id = request.GET.get('task_id', None)
        if task_id is not None:
            task_id = task_id[:-1]
            #print(task_id)
        status = scrapyd.job_status('default', task_id)
        #print(status)
        if status == 'finished':
            with open(r"C:\Users\dmanojlovic\Documents\django_random_movie_generator\src\movie_generator\scrape_top_movies\result.json") as f:
                jso = json.load(f)
            #print('ovo je id', jso[0].get('jobid'))
            data['jsi'] = jso
            data['status'] = status
            #print(data)
            return JsonResponse(data)
    #print('task na dnu',task)
    return render(request, 'rand_movie_gen/index.html', {})

def home(request):
    return render(request, 'rand_movie_gen/home.html', {})


# from scrape_top_movies.scrape_top_movies.spiders.scrape_movies import TopRatedMovies
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings
# from scrapy.signalmanager import dispatcher
# from scrapy import signals
#
#
# process = CrawlerProcess(get_project_settings())

# var = name of spider

# process.crawl(TopRatedMovie)
# process.start()
