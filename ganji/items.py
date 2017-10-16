# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
   title=scrapy.Field()
   Type=scrapy.Field()
   huxing=scrapy.Field()
   area=scrapy.Field()
   towards=scrapy.Field()
   floot=scrapy.Field()
   decorate=scrapy.Field()
   link=scrapy.Field()
   time=scrapy.Field()
   rent=scrapy.Field()