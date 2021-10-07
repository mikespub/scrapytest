import sys

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
	from scrapy.crawler import CrawlerProcess
	from scrapy.utils.project import get_project_settings
	process = CrawlerProcess(get_project_settings())
	# 'site_file' is the name of one of the spiders of the project.
	if len(sys.argv) > 1 and '/' in sys.argv[1]:
		process.crawl('site_file', base_dir=sys.argv[1])
	else:
		process.crawl('site_file', base_dir='/var/www/html')
	process.start() # the script will block here until the crawling is finished

def get_stats():
	import pstats
	file = 'file_stats'
	sortby = 'cumulative'
	p = pstats.Stats(file)
	p.sort_stats(sortby).print_stats()


if __name__ == '__main__':
	#main_profile()
	#python -m cProfile -o file_stats test_file.py
	main()
	#get_stats()
