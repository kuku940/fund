# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from fund.items import FundItem

class FundSpider(CrawlSpider):
	start_urls = []
	for i in range(1,19):
		start_urls.append("https://list.lu.com/list/fund?subType=&haitongGrade=4&fundGroupId=&currentPage="+str(i)+"&orderType=this_year_increase_desc&searchWord=#sortTab")

	# 定义spider名字的字符串(string),一般取值为站点的域名，如xiaoyu.com -> xiaoyu
	name = "fund"
	
	#設置延時
	download_delay = 2
	
	# 包含了spider允许爬取的域名(domain)列表(list)
	# 当 OffsiteMiddleware 启用时， 域名不在列表中的URL不会被跟进。
	allowed_domains = ["list.lu.com"]

	# 当没有制定特定的URL时，spider将从该列表中开始进行爬取
	# start_urls = ["https://list.lu.com/list/fund?subType=&haitongGrade=&fundGroupId=&currentPage=1&orderType=one_month_increase_desc&searchWord=#sortTab"]

	rules = (
		#将所有符合正则表达式的url加入到抓取列表中
		Rule(LinkExtractor(allow=(r"https://list.lu.com/list/fund?subType=&haitongGrade=&fundGroupId=&currentPage=\d+&orderType=one_month_increase_desc&searchWord=#sortTab",))),
		#将所有符合正则表达式的url请求后下载网页代码, 形成response后调用自定义回调函数
		Rule(LinkExtractor(allow=(r"\S+productDetail\S+",)),callback="parse_item"),
	)
	
	def parse_item(self,response):
		#self.log("======>>>>>>:" + response.url)
		sel = Selector(response)	

		item = FundItem()

		# 通过css来获取值
		item['product_name'] = sel.css('div[class*=product-name]::text').extract()[0].strip().encode('utf8')
		item['product_code'] = sel.css('div[class*=product-code]::text').extract()[0].strip().encode('gbk').split("：")[1].decode("gbk").encode("utf8")

		item['product_company'] = sel.xpath('//ul[@class="fund-info clearfix"]/li[3]/b/text()').extract()[0].strip().encode('utf8')
		item['fund_manager'] = sel.xpath('//p[@class="manager-icon"]/span/text()').extract()[0].strip().encode('utf8')
		
		# 通过xpath来获取值,也可以使用正则表达式来获取值
		item['product_type'] = sel.xpath('//ul[@class="fund-info clearfix"]/li[4]/b/text()').extract()[0].strip().encode('utf8')
		item['venture_grade'] = sel.xpath('//div[@class="venture-grade"][1]/span/text()').extract()[0].strip().encode("utf8")
		item['setup_day'] = sel.xpath('//ul[@class="fund-info clearfix"]/li[8]/b/text()').extract()[0].strip().encode('utf8')
		item['product_scale'] = sel.xpath('//ul[@class="fund-info clearfix"]/li[10]/b/text()').extract()[0].strip().encode('gbk')[:-4].decode("gbk").encode("utf8")


		# 计算每年的成长与同类比较值
		item['self_increase_month'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[1]/td[3]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['self_increase_quarter'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[1]/td[4]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['self_increase_one_year'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[1]/td[5]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['self_increase_two_year'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[1]/td[6]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")


		item['similar_increase_month'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[2]/td[3]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['similar_increase_quarter'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[2]/td[4]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['similar_increase_one_year'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[2]/td[5]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")
		item['similar_increase_two_year'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[2]/td[6]/span/text()').extract()[0].strip().encode('gbk')[:-1].decode("gbk").encode("utf8")


		item['month_rank'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[3]/td[3]/text()').extract()[0].strip().encode("utf8")
		item['quarter_rank'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[3]/td[4]/text()').extract()[0].strip().encode("utf8")
		item['one_year_rank'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[3]/td[5]/text()').extract()[0].strip().encode("utf8")
		item['two_year_rank'] = sel.xpath('//table[@class="product-table phase-increase-table"]/tbody/tr[3]/td[6]/text()').extract()[0].strip().encode("utf8")

		return item