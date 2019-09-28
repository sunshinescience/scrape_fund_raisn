# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #campaign_message = scrapy.Field()
    #owner_name = scrapy.Field()
    #category = scrapy.Field()
    raised_progress = scrapy.Field()
    goal = scrapy.Field()
    campaign_title = scrapy.Field()
    currency_symbol = scrapy.Field()
    amount_raised = scrapy.Field()
    duration_running = scrapy.Field()
    duration_label = scrapy.Field()
    number_contributers = scrapy.Field()
    location = scrapy.Field()
    owner_name = scrapy.Field()
    datetime = scrapy.Field()
    
    
