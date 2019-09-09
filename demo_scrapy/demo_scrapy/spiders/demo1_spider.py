import scrapy

class CrowdfundSpider(scrapy.Spider): # Use the Spider class provided by Scrapy and make a subclass out of it called CrowdfundSpider
    name = "indiegogo_audio" # This is the name of the spider, which will be used to run the spider when `scrapy crawl name_of_spider` is used
    start_urls = ["https://www.indiegogo.com/explore/audio?project_type=campaign&project_timing=all&sort=trending"]

def parse(self, response):
    campaign_SELECTOR = '.discoverableCard'
    for campaign in response.css(campaign_SELECTOR):
        pass
