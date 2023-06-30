```python
import scrapy
from scrapy.loader import ItemLoader
from web_scraper.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        self.log('Visited %s' % response.url)
        reddit_posts = response.css('div.thing')
        for post in reddit_posts:
            loader = ItemLoader(item=RedditItem(), selector=post)
            loader.add_css('title', 'a.title ::text')
            loader.add_css('url', 'a.title ::attr(href)')
            loader.add_css('upvotes', 'div.score.unvoted ::text')
            loader.add_css('comments', 'a.comments ::text')
            yield loader.load_item()

        # Pagination
        next_page = response.css('span.next-button a ::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
```