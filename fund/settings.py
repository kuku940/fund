# -*- coding: utf-8 -*-

# Scrapy settings for fund project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'fund'

SPIDER_MODULES = ['fund.spiders']
NEWSPIDER_MODULE = 'fund.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'fund (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'fund.pipelines.FundPipeline': 1,
}