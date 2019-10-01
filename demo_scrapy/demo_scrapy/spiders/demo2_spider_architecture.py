import scrapy
from scrapy.loader import ItemLoader
from demo_scrapy.items import DemoScrapyItem
from datetime import datetime

class CrowdfundSpider(scrapy.Spider):
    name = 'fundrazr_campaigns3'
    allowed_domains = ["fundrazr.com"]
    start_urls = [
                'https://fundrazr.com/find?category=Accidents',
                'https://fundrazr.com/find?category=Alumni',
                'https://fundrazr.com/find?category=Animals',
                'https://fundrazr.com/find?category=Arts',
                'https://fundrazr.com/find?category=Business',
                'https://fundrazr.com/find?category=Celebrations',
                'https://fundrazr.com/find?category=Community',
                'https://fundrazr.com/find?category=Education',
                'https://fundrazr.com/find?category=Faith',
                'https://fundrazr.com/find?category=Family',
                'https://fundrazr.com/find?category=Health',
                'https://fundrazr.com/find?category=Legal',
                'https://fundrazr.com/find?category=Memorials',
                'https://fundrazr.com/find?category=Non-profits',
                'https://fundrazr.com/find?category=Politics',
                'https://fundrazr.com/find?category=Sports',
                'https://fundrazr.com/find?category=Travel',
                'https://fundrazr.com/find?category=Veterans',
                'https://fundrazr.com/find?category=Accidents',
                'https://fundrazr.com/find?category=Alumni',
                'https://fundrazr.com/find?category=Animals',
                'https://fundrazr.com/find?category=Arts',
                'https://fundrazr.com/find?category=Business',
                'https://fundrazr.com/find?category=Celebrations',
                'https://fundrazr.com/find?category=Community',
                'https://fundrazr.com/find?category=Education',
                'https://fundrazr.com/find?category=Faith',
                'https://fundrazr.com/find?category=Family',
                'https://fundrazr.com/find?category=Health',
                'https://fundrazr.com/find?category=Legal',
                'https://fundrazr.com/find?category=Memorials',
                'https://fundrazr.com/find?category=Non-profits',
                'https://fundrazr.com/find?category=Politics',
                'https://fundrazr.com/find?category=Sports',
                'https://fundrazr.com/find?category=Travel',
                'https://fundrazr.com/find?category=Veterans'
                ]

    def parse(self, response):
        for href in response.xpath('//h2//a[@class="campaign-link"]/@href'):
            url = "https:" + href.extract()
            yield scrapy.Request(url, callback=self.parse_campaign)
        
        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url) # Scrapy uses requests to ask for a page and gets responses from the webserver. 
        
        # Here, we could add in another Request with a callback to follow another link (if, for example, there was a link in an individual campaign in this example). And the callback here could go to another function that would then parse that followed link.

    def parse_campaign(self, response):
        l = ItemLoader(item=DemoScrapyItem(), repsonse=response)

        # Getting the campaign description
        message = response.xpath("//div[contains(@id, 'full-story')]//text()").extract()
        campaign_msg = []
        for i in message:
            if len(i.strip()) > 0:
                campaign_msg.append(i.strip())
        campaign_message = (''.join(campaign_msg))
        l.add_value('campaign_message', campaign_message)

        # Getting the campaign title
        campaign_title = (response.xpath('//div[@id="campaign-title"]/text()').extract_first()).strip()
        l.add_value('campaign_title', campaign_title)

        # Getting the owner name
        owner_name = response.xpath('//span/a[@class="name subtle-link bold"]/text()').extract_first()
        l.add_value('owner_name', owner_name)

        # Getting the url
        url = response.xpath('//meta[@property="og:url"]/@content').extract_first()
        l.add_value('url', url)


        # Getting the rest of the data from the campaigns
        try:
            raised_progress = response.xpath('//span[@class="raised-progress"]/text()').extract_first()
            goal = ((response.xpath('//*[@id="campaign-stats"]/div[1]/span[3]/text()[2]').extract_first()).strip()).split(' ')[1]
            currency_symbol = response.xpath('//span[@class="currency-symbol"]/text()').extract_first()
            currency_raised = response.xpath('//span[@class="amount-raised"]/text()').extract_first()
            duration_running = response.xpath('//span[@class="stat"]/text()').extract_first() 
            duration_running_label = (response.xpath('//*[@id="campaign-stats"]/div[3]/span/span[2]/text()').extract()[0]).strip()
            number_contributers = response.xpath('//span[@class="donation-count stat"]/text()').extract_first() 
            location = response.xpath('//span/a[@class="muted nowrap"]/text()').extract_first()
            timestamp = (response.xpath('//span[@class="stats-label"]/a/@data-timestamp').extract_first()).rstrip("0") # Getting the timestamp and removing trailing zeros
            datetime_object = datetime.fromtimestamp(int(timestamp))
            hour_launched = (str(datetime_object.hour))
            month_launched = (str(datetime_object.month))
            day_launched = (str(datetime_object.day))
            day_of_week_launched = (str(datetime_object.weekday()))
            
            l.add_value('raised_progress', raised_progress)
            l.add_value('goal', goal)
            l.add_value('currency_symbol', currency_symbol)
            l.add_value('currency_raised', currency_raised)
            l.add_value('duration_running', duration_running)
            l.add_value('duration_running_label', duration_running_label)
            l.add_value('number_contributers', number_contributers)
            l.add_value('location', location)
            #l.add_value('timestamp', timestamp)
            l.add_value('hour_launched', hour_launched)
            #l.add_value('datetime_object', datetime_object)
            l.add_value('month_launched', month_launched)
            l.add_value('day_launched', day_launched)
            l.add_value('day_of_week_launched', day_of_week_launched)
        except:
            pass

        return l.load_item()
 