import scrapy
from jsonpath import jsonpath


class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['spa5.scrape.center']
    start_urls = ['https://spa5.scrape.center/api/book/']

    def start_requests(self):
        for page_num in range(0, 503):
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
            }
            yield scrapy.Request(
                url=self.start_urls[0] + f'?limit=18&offset={page_num*18}',
                dont_filter=True
            )

    def parse(self, response):
        print(jsonpath(response.json(), '$.results.*.name'))



if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute('scrapy crawl bookspider'.split(' '))
