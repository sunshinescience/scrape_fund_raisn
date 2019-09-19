import scrapy


class CrowdfundSpider(scrapy.Spider):
    name = "fundrazr_campaigns"
    allowed_domains = ["fundrazr.com"]
    start_urls = [
        'https://fundrazr.com/find?category=Accidents'
    ]

    def parse(self, response):
        widget_tall = response.xpath('//*[@class="widget tall"]')
        for campaign in widget_tall:
            campaign_message = campaign.xpath('.//@data-message').extract() # Use extract_first() to get only the first campaign
            owner_name = campaign.xpath('.//@data-ownername').extract()
            
            yield{'Campaign message': campaign_message, 'Owner name' : owner_name}
            
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

