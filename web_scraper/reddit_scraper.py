```python
import scrapy
from scrapy.crawler import CrawlerProcess
from .spiders.reddit_spider import RedditSpider

class RedditScraper:

    def __init__(self):
        self.process = CrawlerProcess(settings={
            'FEED_FORMAT': 'json',
            'FEED_URI': 'output.json'
        })

    def run_spider(self):
        self.process.crawl(RedditSpider)
        self.process.start()

if __name__ == "__main__":
    scraper = RedditScraper()
    scraper.run_spider()
```