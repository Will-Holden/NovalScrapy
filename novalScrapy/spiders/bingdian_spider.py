#bingdian.py
#-*- coding:utf-8 -*-
import scrapy
from novalScrapy.items import DcontentItem,NovalscrapyItem
from novalScrapy.SQLitepipelines.sql import Sql

class novalSpider(scrapy.Spider):
    name = "noval"
    allowed_domains = ['23us.com']
	start_urls = [
	        'http://www.23us.com/class/1_1.html',
	        'http://www.23wx.com/class/2_1.html',
	        'http://www.23wx.com/class/3_1.html',
	        'http://www.23wx.com/class/4_1.html',
	        'http://www.23wx.com/class/5_1.html',
	        'http://www.23wx.com/class/6_1.html',
	        'http://www.23wx.com/class/7_1.html',
	        'http://www.23wx.com/class/8_1.html',
	        'http://www.23wx.com/class/9_1.html',
	        'http://www.23wx.com/class/10_1.html'
	    ]
	def parse(self, response):
		books = reponse.xpath('//dd/table/tr[@bgcolor="#FFFFF"]')
		print (books.extract())
		for book in books:
			name = book.xpath('.//td[1]/a[2]/text()').extract()[0]
		    author = book.xpath('.//td[3]/text()').extract()[0]
            novelurl = book.xpath('.//td[1]/a[2]/@href').extract()[0]
            serialstatus = book.xpath('.//td[6]/text()').extract()[0]
            serialnumber = book.xpath('.//td[4]/text()').extract()[0]
            category = book.xpath('//dl/dt/h2/text()').re(u'(.+) - 文章列表')[0]
            jianjieurl = book.xpath('.//td[1]/a[1]/@href').extract()[0]

            item = BingdianItem()
            item['name'] =  name
            item['author'] = author
            item['novelurl'] = novelurl
            item['serialstatus'] = serialstatus
            item['serialnumber'] = serialnumber
            item['category'] = category
            item['name_id'] = jianjieurl.split('/')[-1]

            yield item
            yield scrapy.Request(novelurl,callback = self.get_chapter,meta = {'name_id' : item['name_id']})

        next_page = response.xpath('//dd[@class="pages"]/div/a[12]/@href').extract()[0] #获取下一页地址
        if next_page:
            yield  scrapy.Request(next_page)

	def get_chapter(self,response):
		num = 0
		allurls = reponse.xpath('//tr')
		for trurls in allurls:
			tdurls = trurls.xpath('.//td[@class="L"]')
			for url in urls:
				num = num + 1
				chapterurl = response.url +  url.xpath('.//a/@href').extract()[0]

