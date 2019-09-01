import scrapy

class CrowdfundSpider(scrapy.Spider): # Use the Spider class provided by Scrapy and make a subclass out of it called CrowdfundSpider
    name = "indiegogo_audio" # This is the name of the spider, which will be used to run the spider when `scrapy crawl name_of_spider` is used
    start_urls = ["https://www.indiegogo.com/projects/pamu-slide-born-for-music-never-fall-out#/"]


