import scrapy


class SiteLocalSpider(scrapy.Spider):
	name = 'site_local'
	allowed_domains = ['localhost']
	start_urls = ['http://localhost:8000/']

	def parse(self, response):
		print response.url
