
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from ssaberi.spiders.image_crawl_spider import ImageCrawlSpiderSpider


process = CrawlerProcess(get_project_settings())
process.crawl(ImageCrawlSpiderSpider)
process.start()
