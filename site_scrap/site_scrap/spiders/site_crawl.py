import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SiteCrawlSpider(CrawlSpider):
	name = 'site_crawl'
	allowed_domains = ['localhost']
	# Start local webserver with python -m http.server or python -m SimpleHTTPServer if needed
	start_urls = ['http://localhost:8000/']

	rules = (
		Rule(LinkExtractor(allow=r'/$'), follow=True),
		Rule(LinkExtractor(allow=r'\.html?$'), callback='parse_item', follow=True),
		#Rule(LinkExtractor(allow=r'Item/'), callback='parse_item', process_links='filter_links', follow=False),
	)

	#def filter_links(self, links):
	#	for link in links:
	#		#print link
	#		yield link

	def parse_item(self, response):
		#print 'Parsing', response.url
		i = {}
		#i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
		#i['name'] = response.xpath('//div[@id="name"]').extract()
		#i['description'] = response.xpath('//div[@id="description"]').extract()
		return i
