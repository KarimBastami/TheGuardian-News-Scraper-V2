# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TheguardianSpider(CrawlSpider):
    name = 'theguardian'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com//world/all/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//a[contains(@class, 'fc-item__link')]"), callback='parse_item', follow=False),
        
        Rule(LinkExtractor(restrict_xpaths= "//a[contains(@class,'pagination__action--static') and contains(@rel,'next')]"), follow=True),
    )

    def parse_item(self, response):

        articleUrl = response.url
        articleTitle = response.xpath("normalize-space(//h1/ text())").get()
        articleCategory = response.xpath("normalize-space(//a[@data-link-name='article section'] / * / text())").get()
        articleAuthor = response.xpath("normalize-space(//a[@rel ='author'] / text())").get()
        articleText = ""
        articleType = ""

        # --------------------------------------------------------------------------------------------------------

        if ("live" in articleUrl):
            articleText = "This is a Live Feed, check website for comments and text content"
            articleType = "Live"

        else:
            articleText = response.xpath("//div[contains(@class , 'article-body-commercial-selector')] / p / text()").getall()

            articleType = "Normal"

            if (not articleText):
                articleText = response.xpath("//*[contains(@class , 'content__standfirst content__standfirst--gallery')] / p / text()").getall()
                articleType = "Pictures"

            if (not articleText):
                articleText = response.xpath("//*[@class = 'content__standfirst'] / p[1] / text()").getall()
                articleType = "Video"

            if (not articleText):
                articleText = "No Text Content"
                articleType = "Unidentifed Type"
        
        # --------------------------------------------------------------------------------------------------------


        if (not articleCategory):
            articleCategory = "No Category"

        # --------------------------------------------------------------------------------------------------------


        if (not articleAuthor):
            articleAuthor = response.xpath("normalize-space(//address [@aria-label = 'Contributor info'] / * / text())").get()


        if (not articleAuthor):
            articleAuthorContainers = response.xpath("//span[@itemprop='name']")

            for container in articleAuthorContainers:
                articleAuthor += container.xpath(".//text()").get() + ", "
        

        if (not articleAuthor):
            articleAuthor = response.xpath("//*[@class = 'byline'] / text()").get()


        if (not articleAuthor):
            articleAuthor = "No Author"

        # --------------------------------------------------------------------------------------------------------

        print("PAGE #", response.xpath("//span[@aria-label = 'Current page'] / text()").get())

        yield {

            "Url" : articleUrl,
            "Title" : articleTitle,
            "Author" : articleAuthor,
            "Category" : articleCategory,
            "Article Type" : articleType,
            "Text Content" : articleText
        }


         
