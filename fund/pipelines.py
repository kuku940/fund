# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb

# 数据库链接方法
def ConnectDB():
	conn = MySQLdb.connect(host='localhost',user='root',passwd='xiaode',db='spider',port=3306,charset='utf8')
	return conn

class FundPipeline(object):
	def process_item(self, item, spider):
		#for key in item:
			#print key,":",item[key]

		# 链接数据库 并存入数据库中
		conn = ConnectDB()
		cur = conn.cursor()
		
		cur.execute("select product_code from fund where product_code = %s",(item['product_code'],))
		result = cur.fetchone()
		
		if result is None:
			cur.execute("insert into fund (product_code,product_name,product_type,venture_grade,setup_day,product_scale,product_company,fund_manager,self_increase_month,self_increase_quarter,self_increase_one_year,self_increase_two_year,similar_increase_month,similar_increase_quarter,similar_increase_one_year,similar_increase_two_year,month_rank,quarter_rank,one_year_rank,two_year_rank) \
				values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['product_code'],item['product_name'],item['product_type'],item['venture_grade'],item['setup_day'],str(item['product_scale']),item['product_company'],item['fund_manager'],str(item['self_increase_month']),str(item['self_increase_quarter']),str(item["self_increase_one_year"]),str(item["self_increase_two_year"]),str(item['similar_increase_month']),str(item['similar_increase_quarter']),str(item["similar_increase_one_year"]),str(item["similar_increase_two_year"]),str(item['month_rank']),str(item['quarter_rank']),str(item["one_year_rank"]),str(item["two_year_rank"])))
			print "基金代码："+str(item['product_code'])+"捕获"

		else:
			cur.execute("update fund set product_name=%s,product_type=%s,venture_grade=%s,setup_day=%s,product_scale=%s,product_company=%s,fund_manager=%s,self_increase_month=%s,self_increase_quarter=%s,self_increase_one_year=%s,self_increase_two_year=%s,similar_increase_month=%s,similar_increase_quarter=%s,similar_increase_one_year=%s,similar_increase_two_year=%s,month_rank=%s,quarter_rank=%s,one_year_rank=%s,two_year_rank=%s where \
				product_code = %s",(item['product_name'],item['product_type'],item['venture_grade'],item['setup_day'],str(item['product_scale']),item['product_company'],item['fund_manager'],str(item['self_increase_month']),str(item['self_increase_quarter']),str(item["self_increase_one_year"]),str(item["self_increase_two_year"]),str(item['similar_increase_month']),str(item['similar_increase_quarter']),str(item["similar_increase_one_year"]),str(item["similar_increase_two_year"]),str(item['month_rank']),str(item['quarter_rank']),str(item["one_year_rank"]),str(item["two_year_rank"]),item['product_code']))
			print "基金代码："+str(item['product_code'])+"更新"

		conn.commit()
		conn.close()	

		return item

class KukuPipeline(object):
	def process_item(self, item, spider):
		print "=====>>>>>"+str(item["url"])

		return item