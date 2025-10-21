import scrapy

class SnpSpider(scrapy.spiders):
    name = "snp"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"]

    def parse(self, response):
        symbol = response.xpath('//tab@id=constituents//td[1]/a/text()').get()
        name = response.xpath('//tab@id=constituents//td[1]/a/text()').get()
        sector = response.xpath('//tab@id=constituents//td[1]/a/text()').get()

    def parse(self, response):




