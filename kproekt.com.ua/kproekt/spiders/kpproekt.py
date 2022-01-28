import scrapy
from kproekt.items import Product
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser as view


class KpproektSpider(scrapy.Spider):
    name = 'kpproekt'
    custom_settings = {'ROBOTSTXT_OBEY': False,
                       "ITEM_PIPELINES": {
        'kproekt.pipelines.KproektPipeline': 300,
    }
    }
    start_urls = ['https://kproekt.com.ua/katalog-produktsii/teplovoe-oborudovanie/parokonvektomaty']

    def parse(self, response):
        product_links = response.xpath('//div[@class="vm-product-descr-container-1"]/h2/a/@href').getall()
        if not product_links:
            raise RuntimeError('Links are not exist')
        for product_link in product_links:
            yield scrapy.Request(
                url='https://kproekt.com.ua' + product_link,
                callback=self.parse_product
            )

    def parse_product(self, response):
        name = response.xpath('//h1[@class="product-detail-title"]/text()').get()
        images = response.xpath('//div[@class="main-image"]/a/img/@data-src').get()
        price = response.xpath('//span[@class="PricesalesPrice"]/text()').get()
        description = response.xpath('//div[@class="product-description"]/p/text()').get()
        if description:
            description_str = "".join(description)
        else:
            description_str = ""
        yield Product(name=name, images=images, price=price, description=description_str, url=response.url)


if __name__ == "__main__":
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(KpproektSpider)
    process.start()  # the script will block here until the crawling is finished
