import scrapy

class MPSpider(scrapy.Spider):
    name = "mp_spider"
    start_urls = ["https://members.parliament.uk/member/400/registeredinterests"]

    custom_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers=self.custom_headers, callback=self.parse)

    def parse(self, response):
        mp_name = response.xpath('//div[@class="hero-banner"]/text()').get()
        
        if mp_name:
            yield {
                'mp_name': mp_name.strip()
            }