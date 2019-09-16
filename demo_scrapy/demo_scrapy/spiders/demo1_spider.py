import scrapy

class CrowdfundSpider(scrapy.Spider): # Use the Spider class provided by Scrapy and make a subclass out of it called CrowdfundSpider
    name = "fundrazr_accidents" # This is the name of the spider, which will be used to run the spider when `scrapy crawl name_of_spider` is used
    start_urls = ["https://fundrazr.com/find?category=Accidents"]

def parse(self, response):
    campaign_titles = response.xpath('//h2//a[starts-with(@href, "//fund")]/text()').extract() 
    urls = []
    for href in response.xpath('//h2//a//@href'):
        url = "https:" + href.extract()
        urls.append(url)

    yield {'Campaign titles': campaign_titles, 'URL': urls}
    