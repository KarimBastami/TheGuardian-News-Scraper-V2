# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo


class MongoDbPipeline(object):

    # @classmethod
    # def from_crawler(cls, crawler): #reference to setting.py file

    collectionName = "News_Articles"


    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://Scrapy_Scraper:BNPKPhu6WpStzAfw@theguardianarticles.zaufd.mongodb.net/TheGuardianArticles?retryWrites=true&w=majority")
        self.db = self.client["TheGuardian"]


    def close_spider(self, spider):
        self.client.close() 


    def process_item(self, item, spider):
        self.db[self.collectionName].insert(item)
        return item

