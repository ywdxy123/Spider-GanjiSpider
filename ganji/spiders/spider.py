import scrapy
from scrapy.http import HtmlResponse
from .. items import GanjiItem
class GanjiSpider(scrapy.Spider):

	name='spider'
	allowed_domains=['http://sh.ganji.com']
	start_urls=['http://sh.ganji.com/fang1/o2/']

	def parse(self,response):
		item=GanjiItem()
		'''
		title=scrapy.Field()
   		Type=scrapy.Field()
   		huxing=scrapy.Field()
   		area=scrapy.Field()
   		towards=scrapy.Field()
   		floot=scrapy.Field()
   		decorate=scrapy.Field()
  		area=scrapy.Field()
   		link=scrapy.Field()
   		rent=scrapy.Field()		
   		'''
		boxes=response.xpath('//*[@id="f_mew_list"]/div[6]/div[1]/div[3]/div[1]/div')
		for box in boxes:
			item['title']=box.xpath("./dl/dd/a/@title").extract()
			item['Type']=box.xpath("./dl/dd[2]/span[1]/text()").extract()
			item['huxing']=box.xpath("/dl/dd[2]/@data-huxing").extract()
			item['area']=box.xpath("./dl/dd[2]/span[5]/text()").extract()
			item['towards']=box.xpath("./dl/dd[2]/span[7]/text()").extract()
			item['floot']=box.xpath("./dl/dd[2]/span[9]/text()").extract()
			item['decorate']=box.xpath("./dl/dd[2]/span[11]/text()").extract()
			item['rent']=box.xpath("./dl/dd[5]/div/span[1]/text()").extract()+box.xpath("./dl/dd[5]/div/span[2]/text()").extract()
			item['time']=box.xpath("./dl/dd[5]/div[2]/text()").extract()
			item['link']=box.xpath('./@href').extract()
			yield item
			
		urls=response.xpath('//*[@id="f_mew_list"]/div[6]/div[1]/div[4]/div/div/ul/li[12]/a/@href').extract()
		'''for url in urls:
			if len(url)>0:
				print(url)
				yield Request(url,callback=self.parse)
				'''
