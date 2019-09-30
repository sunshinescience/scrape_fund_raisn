import scrapy
from scrapy.loader import ItemLoader
from demo_scrapy.items import DemoScrapyItem
from datetime import datetime

class CrowdfundSpider(scrapy.Spider):
    name = 'fundrazr_campaigns3'
    allowed_domains = ["fundrazr.com"]
    start_urls = [
                'https://fundrazr.com/find?category=Accidents'
                ]

    def parse_base_page(self, response):
        category = response.xpath('//li[@class="active"]//a[starts-with(@href, "https://fundrazr.com/find?category=")]/text()').extract()
        yield{'Category': category}

    def parse(self, response):
        for href in response.xpath('//a[@class="campaign-link"]/@href'):
            url = "https:" + href.extract()
            yield scrapy.Request(url, callback=self.parse_campaign)	

    def parse_campaign(self, response):
        l = ItemLoader(item=DemoScrapyItem(), repsonse=response)

        # Obtain the campaign description
        message = response.xpath("//div[contains(@id, 'full-story')]//text()").extract()
        campaign_msg = []
        for i in message:
            if len(i.strip()) > 0:
                campaign_msg.append(i.strip())
        campaign_message = (''.join(campaign_msg))

        raised_progress = response.xpath('//span[@class="raised-progress"]/text()').extract_first()
        goal = ((response.xpath('//*[@id="campaign-stats"]/div[1]/span[3]/text()[2]').extract_first()).strip()).split(' ')[1]
        campaign_title = (response.xpath('//div[@id="campaign-title"]/text()').extract_first()).strip()
        currency_symbol = response.xpath('//span[@class="currency-symbol"]/text()').extract_first()
        amount_raised = response.xpath('//span[@class="amount-raised"]/text()').extract_first()
        duration_running = response.xpath('//span[@class="stat"]/text()').extract_first() 
        duration_label = (response.xpath('//*[@id="campaign-stats"]/div[3]/span/span[2]/text()').extract()[0]).strip()
        number_contributers = response.xpath('//span[@class="donation-count stat"]/text()').extract_first() 
        location = response.xpath('//span/a[@class="muted nowrap"]/text()').extract_first()
        owner_name = response.xpath('//span/a[@class="name subtle-link bold"]/text()').extract_first()
        timestamp = (response.xpath('//span[@class="stats-label"]/a/@data-timestamp').extract_first()).rstrip("0") # Getting the timestamp and removing trailing zeros
        datetime_object = datetime.fromtimestamp(int(timestamp))
        hour_launched = (str(datetime_object.hour))
        month_launched = (str(datetime_object.month))
        day_launched = (str(datetime_object.day))
        day_of_week_launched = (str(datetime_object.weekday()))
        url = response.xpath('//meta[@property="og:url"]/@content').extract_first()

        l.add_value('campaign_message', campaign_message)
        l.add_value('raised_progress', raised_progress)
        l.add_value('goal', goal)
        l.add_value('campaign_title', campaign_title)
        l.add_value('currency_symbol', currency_symbol)
        l.add_value('amount_raised', amount_raised)
        l.add_value('duration_running', duration_running)
        l.add_value('duration_label', duration_label)
        l.add_value('number_contributers', number_contributers)
        l.add_value('location', location)
        l.add_value('owner_name', owner_name)
        #l.add_value('timestamp', timestamp)
        l.add_value('hour_launched', hour_launched)
        #l.add_value('datetime_object', datetime_object)
        l.add_value('month_launched', month_launched)
        l.add_value('day_launched', day_launched)
        l.add_value('day_of_week_launched', day_of_week_launched)
        l.add_value('url', url)

        return l.load_item()

            