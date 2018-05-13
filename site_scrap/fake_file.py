# -*- coding: utf-8 -*-
#
# Parse local files directly instead of going via spider and downloader
# CHECKME: follow similar structure as scrapy spiders, cfr. imdb_local.py
#
import os
import re
import sys
import scrapy


class FakeFileSpider(object):
	name = 'fake_file'
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
				# CHECKME: with regular scrapy, this should return a request
				# for each file, but here we'll parse it directly ourselves
				#yield scrapy.Request('file://' + os.path.join(root, name))
				file = os.path.join(root, name)
				items = self.parse_file(file)
				for item in items:
					yield item

	def parse_file(self, file):
		with open(file, 'rb') as f:
			data = f.read()
			# CHECKME: create response directly from file here
			response = scrapy.http.HtmlResponse(url=file, body=data)
			# CHECKME: this returns a generator, so we need to loop over it
			items = self.parse(response)
			for item in items:
				yield item

	def parse(self, response):
		#print 'Parsing', response.url
		item = {}
		item['file'] = response.url
		yield item


def main_profile():
	import cProfile, pstats, StringIO
	pr = cProfile.Profile()
	pr.enable()
	main()
	pr.disable()
	s = StringIO.StringIO()
	sortby = 'cumulative'
	ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
	ps.print_stats()
	print s.getvalue()

def main():
	spider = FakeFileSpider()
	if len(sys.argv) > 1 and '/' in sys.argv[1]:
		spider.base_dir = sys.argv[1]
	items = spider.start_requests()
	for item in items:
		#print item['file']
		pass


if __name__ == '__main__':
	#main_profile()
	main()
