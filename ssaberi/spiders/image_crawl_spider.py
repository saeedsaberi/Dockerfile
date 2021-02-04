import scrapy
import re
from scrapy.crawler import Crawler
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.project import get_project_settings
from ..items import ImagescraperItem
import numpy as np
# from scrapy.contrib.spiders import CrawlSpider, Rule


class ImageCrawlSpiderSpider( CrawlSpider ):  ##scrapy.Spider ##CrawlSpider
    name = "image_crawl_spider"
    # URLs = [l.strip('"').strip('[').strip(']').split(',') for l in open('urls.txt').readlines()]

    def __init__(self, *args, 
        threads =1, **kwargs):
            super(ImageCrawlSpiderSpider, self).__init__(*args, **kwargs)
            super().__init__(*args, **kwargs)

            # self.crawler.engine.downloader.total_concurrency = threads
            # engine.downloader.total_concurrency = threads
            self.URLs = kwargs.pop('start_urls').strip('"').strip('[').strip(']').split(',') 
            print('These are the input URLs',self.URLs )
            self.threads = np.int( kwargs.pop('threads') )
    def start_requests(self):
        for url in self.URLs :
            yield scrapy.Request(url=url, 
                callback=self.parse_image,
                dont_filter=True) #, self.parse_image)

    # rules = (Rule( #LinkExtractor(allow=r""),
    #                  callback="parse_image", follow=True),)
    rules = (Rule(LinkExtractor(allow=()), callback='parse_image', follow=True),)

    def parse_image(self, response):
        img = response.css("img").xpath("@src")
        if img is not None:
            # imgs = response.xpath('//div[@class="item active"]/img/@src').getall()
            self.crawler.domain_concurrency = self.threads
            imageURLs = img.getall()
            print(imageURLs)
            base= response.url
            print(len(imageURLs))
            print(["".join([base,url])for url in imageURLs ] ) # "".join(url,response.url)
            

            """
            Computing the Absolute path of the image file.
            "image_urls" require absolute path, not relative path
            """
            image = ImagescraperItem()
            image["image_urls"] = ["".join([base,url]) for url in imageURLs ]   # "image_urls" must be a list
            image["page_url"] = base
            yield image
