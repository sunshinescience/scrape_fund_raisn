import scrapy
from scrapy.loader import ItemLoader
from demo_scrapy.items import DemoScrapyItem

class CrowdfundSpider(scrapy.Spider):
    name = 'fundrazr_campaigns3'
    allowed_domains = ["fundrazr.com"]
    start_urls = [
                'https://fundrazr.com/find?category=Accidents'
                ]

    def parse(self, response):
        l = ItemLoader(item=DemoScrapyItem(), repsonse=response)
        campaign_message = response.xpath('.//@data-message').extract() 
        owner_name = response.xpath('.//@data-ownername').extract()

        l.add_value('campaign_message', campaign_message)
        l.add_value('owner_name', owner_name)

        return l.load_item()

            