from django.urls import path, include, re_path
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .views import (index)

app_name = 'rand_movie_gen' # za url putanju do appa

urlpatterns = [
     path('index/', index, name='index'),
     path('api/crawl/', index, name='index'),

]
