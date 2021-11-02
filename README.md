# django-random-movie-generator
This app is connected with scrape-movies app to pick random movie. To connect django and scrape site we use scrapyd (https://scrapyd.readthedocs.io/en/stable/index.html) which is an app (typically run as a daemon) that 
listens to requests for spiders to run and spawns a process for each one, which basically executes: scrapy crawl myspider
