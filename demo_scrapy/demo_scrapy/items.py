# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DemoScrapyItem(scrapy.Item):
    campaign_message = scrapy.Field()
    
    #category = scrapy.Field()
    raised_progress = scrapy.Field()
    goal = scrapy.Field()
    campaign_title = scrapy.Field()
    currency_symbol = scrapy.Field()
    currency_raised = scrapy.Field()
    duration_running = scrapy.Field()
    duration_running_label = scrapy.Field()
    number_contributers = scrapy.Field()
    location = scrapy.Field()
    owner_name = scrapy.Field()
    hour_launched = scrapy.Field()
    month_launched = scrapy.Field()
    day_launched = scrapy.Field()
    day_of_week_launched = scrapy.Field()
    url = scrapy.Field()
    
    