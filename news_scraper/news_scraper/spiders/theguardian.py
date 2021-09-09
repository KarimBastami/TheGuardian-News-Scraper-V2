# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TheguardianSpider(CrawlSpider):
    name = 'theguardian'
    allowed_domains = ['www.theguardian.com']
    start_urls = ['https://www.theguardian.com//world/all/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths= "//a[contains(@class, 'fc-item__link')]"), callback='parse_item', follow=True),
        
        # Rule(LinkExtractor(restrict_xpaths= "//a[contains(@class,'pagination__action--static') and contains(@rel,'next')]"), follow=True),
    )

    def parse_item(self, response):

        articleUrl = response.url
        articleTitle = response.xpath("normalize-space(//h1/ text())").get()
        articleCategory = response.xpath("normalize-space(//a[@data-link-name='article section'] / * / text())").get()
        articleAuthor = response.xpath("normalize-space(//a[@rel ='author'] / text())").get()


        if ("live" in articleUrl):
            articleText = "This is a Live Feed, check website for comments and text content"
        
        else:
            articleText = response.xpath("//div[contains(@class , 'article-body-commercial-selector')] / p / text()").getall()

            print("LENGTH1:----------", len(articleText))

            if (len(articleText) == 0):
                print("LENGTH2:----------", len(articleText))
                articleText = response.xpath("//*[contains(@class , 'content__standfirst content__standfirst--gallery')] / p / text()").getall()

            if (len(articleText) == 0):
                print("LENGTH3:----------", len(articleText))
                articleText = response.xpath("//*[@class = 'content__standfirst'] / p[1] / text()").get()

            if (len(articleText) == 0):
                articleText = "No Text Content"
        
            


        if (len(articleCategory) == 0):
            articleCategory = "No Category"



        if (len(articleAuthor) == 0):
            articleAuthor = response.xpath("normalize-space(//address [@aria-label = 'Contributor info'] / * / text())").get()


        if (len(articleAuthor) == 0):
            articleAuthorContainers = response.xpath("//span[@itemprop='name']")

            for container in articleAuthorContainers:
                articleAuthor += container.xpath(".//text()").get() + ", "
        

        if (len(articleAuthor) == 0):
            articleAuthor = response.xpath("//*[@class = 'byline'] / text()").get()


        if (len(articleAuthor) == 0):
            articleAuthor = "No Author"


        yield {

            "Url" : articleUrl,
            "Title" : articleTitle,
            "Author" : articleAuthor,
            "Category" : articleCategory,
            "Text Content" : articleText
        }


         
