# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	product_code = scrapy.Field()		# �������
	product_name = scrapy.Field()		# ��������
	product_company = scrapy.Field()	# ����˾
	fund_manager = scrapy.Field()		# ������
	
	product_type = scrapy.Field()		# ��������
	venture_grade = scrapy.Field()		# ���յȼ�
	setup_day = scrapy.Field()			# ��������
	product_scale = scrapy.Field()		# �����ģ

	# �����������
	self_increase_month = scrapy.Field()		# һ���µ��������
	self_increase_quarter = scrapy.Field()		# һ�����ȵ��������
	self_increase_one_year = scrapy.Field()		# һ�����������
	self_increase_two_year = scrapy.Field()		# �������������

	similar_increase_month = scrapy.Field()		# ͬ��һ���µ��������
	similar_increase_quarter = scrapy.Field()	# ͬ��һ�����ȵ��������
	similar_increase_one_year = scrapy.Field()	# ͬ��һ�����������
	similar_increase_two_year = scrapy.Field()	# ͬ���������������

	month_rank = scrapy.Field()					# һ���µ�����
	quarter_rank = scrapy.Field()				# һ�����ȵ�����
	one_year_rank = scrapy.Field()				# һ�����������
	two_year_rank = scrapy.Field()				# �������������

class KukuItem(scrapy.Item):
	url = scrapy.Field()