import scrapy

class CrowdfundSpider(scrapy.Spider):
    name = "fundrazr_campaigns2"
    allowed_domains = ["fundrazr.com"]
    start_urls = [
        'https://fundrazr.com/find?category=Accidents'
    ]

    def parse(self, response):
        category = response.xpath('//li[@class="active"]//a[starts-with(@href, "https://fundrazr.com/find?category=")]/text()').extract()
        widget_tall = response.xpath('//*[@class="widget tall"]')   

        for campaign in widget_tall:
            campaign_message = campaign.xpath('.//@data-message').extract() # Use extract_first() to get only the first campaign
            owner_name = campaign.xpath('.//@data-ownername').extract()
            location = campaign.xpath('.//p[@class="location"]/text()').extract()
            campaign_title = campaign.xpath('.//h2//a[starts-with(@href, "//fund")]/text()').extract()   
            
            currency_symbol = campaign.xpath('.//div[@class="clearfix stats-entries"]/div[1]/p[@class="stats-value"]/span/text()').extract()
            amount_raised = campaign.xpath('.//div[@class="clearfix stats-entries"]/div[1]/p[@class="stats-value"]/text()').extract()
            
            duration_running = campaign.xpath('.//div[@class="clearfix stats-entries"]/div[2]/p[@class="stats-value"]/text()').extract()
            duration_label = campaign.xpath('.//div[@class="clearfix stats-entries"]/div[2]/p[@class="stats-label"]/text()').extract()

            url = []
            for href in campaign.xpath('.//@data-campaignurl'):
                base_url = "https:" + href.extract()
                url.append(base_url)

            yield{'Category': category, 'Campaign title': campaign_title, 'Owner name' : owner_name, 'Location': location, 'Currency symbol': currency_symbol, 'Amount raised': amount_raised, 'Duration running': duration_running, 'Duration running label': duration_label, 'URL': url, 'Campaign description': campaign_message}

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

