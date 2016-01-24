# -*- coding: utf-8 -*-

import sys
reload(sys)
# python默认的环境编码是ascii
sys.setdefaultencoding("utf-8")

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from fund.items import KukuItem

class KukuSpider(CrawlSpider):
	start_urls = []

	# 定义spider名字的字符串(string),一般取值为站点的域名，如xiaoyu.com -> xiaoyu
	name = "kuku"
	
	#設置延時
	download_delay = 1
	
	# 包含了spider允许爬取的域名(domain)列表(list)
	# 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。
	allowed_domains = ["kuku940.github.io"]

	# 当没有制定特定的URL时，spider将从该列表中开始进行爬取
	start_urls = ["http://kuku940.github.io/"]

	rules = (
		#将所有符合正则表达式的url加入到抓取列表中
		Rule(LinkExtractor(allow=(r"http://kuku940.github.io/page/\d+/",))),
		#将所有符合正则表达式的url请求后下载网页代码, 形成response后调用自定义回调函数
		Rule(LinkExtractor(allow=(r"\S+kuku940.github.io/\d{4}/\d{2}/\d{2}/\S+",)),callback="parse_item"),
	)
	
	def parse_item(self,response):
		self.log("======>>>>>>:" + response.url)
		#sel = Selector(response)

		item = KukuItem()

		item["url"] = response.url

		return item