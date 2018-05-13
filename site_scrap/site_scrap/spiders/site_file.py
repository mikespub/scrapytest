# -*- coding: utf-8 -*-
import os
import re
import scrapy


class SiteFileSpider(scrapy.Spider):
	name = 'site_file'
	#allowed_domains = ['file:///var/www/html']
	#start_urls = ['file:///var/www/html/index.html']
	custom_settings = {
		'ROBOTSTXT_OBEY': False,
	}
	# Override base_dir with scrapy crawl site_file -a base_dir=...
	base_dir = '/var/www/html'
	file_ext = r'\.html?$'

	def start_requests(self):
		pattern = re.compile(self.file_ext)
		for root, dirs, files in os.walk(self.base_dir):
			for name in files:
				if not pattern.search(name):
					continue
				yield scrapy.Request('file://' + os.path.join(root, name))

	def parse(self, response):
		#print 'Parsing', response.url
		pass
