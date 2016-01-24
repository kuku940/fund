# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	product_code = scrapy.Field()		# 基金代码
	product_name = scrapy.Field()		# 基金名称
	product_company = scrapy.Field()	# 基金公司
	fund_manager = scrapy.Field()		# 基金经理
	
	product_type = scrapy.Field()		# 基金类型
	venture_grade = scrapy.Field()		# 风险等级
	setup_day = scrapy.Field()			# 成立日期
	product_scale = scrapy.Field()		# 基金规模

	# 基金增长情况
	self_increase_month = scrapy.Field()		# 一个月的增长情况
	self_increase_quarter = scrapy.Field()		# 一个季度的增长情况
	self_increase_one_year = scrapy.Field()		# 一年增长的情况
	self_increase_two_year = scrapy.Field()		# 两年增长的情况

	similar_increase_month = scrapy.Field()		# 同类一个月的增长情况
	similar_increase_quarter = scrapy.Field()	# 同类一个季度的增长情况
	similar_increase_one_year = scrapy.Field()	# 同类一年增长的情况
	similar_increase_two_year = scrapy.Field()	# 同类两年增长的情况

	month_rank = scrapy.Field()					# 一个月的排名
	quarter_rank = scrapy.Field()				# 一个季度的排名
	one_year_rank = scrapy.Field()				# 一年的增长排名
	two_year_rank = scrapy.Field()				# 两年的增长排名

class KukuItem(scrapy.Item):
	url = scrapy.Field()