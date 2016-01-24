# -*- coding: utf-8 -*-

import sys
reload(sys)
# pythonĬ�ϵĻ���������ascii
sys.setdefaultencoding("utf-8")

import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from fund.items import KukuItem

class KukuSpider(CrawlSpider):
	start_urls = []

	# ����spider���ֵ��ַ���(string),һ��ȡֵΪվ�����������xiaoyu.com -> xiaoyu
	name = "kuku"
	
	#�O���ӕr
	download_delay = 1
	
	# ������spider������ȡ������(domain)�б�(list)
	# �� OffsiteMiddleware ����ʱ�� ���������б��е�URL���ᱻ������
	allowed_domains = ["kuku940.github.io"]

	# ��û���ƶ��ض���URLʱ��spider���Ӹ��б��п�ʼ������ȡ
	start_urls = ["http://kuku940.github.io/"]

	rules = (
		#�����з���������ʽ��url���뵽ץȡ�б���
		Rule(LinkExtractor(allow=(r"http://kuku940.github.io/page/\d+/",))),
		#�����з���������ʽ��url�����������ҳ����, �γ�response������Զ���ص�����
		Rule(LinkExtractor(allow=(r"\S+kuku940.github.io/\d{4}/\d{2}/\d{2}/\S+",)),callback="parse_item"),
	)
	
	def parse_item(self,response):
		self.log("======>>>>>>:" + response.url)
		#sel = Selector(response)

		item = KukuItem()

		item["url"] = response.url

		return item