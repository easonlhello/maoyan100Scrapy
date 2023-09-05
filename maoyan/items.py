# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # 下面是要获取到数据
    # define the fields for your item here like:
    # 排名
    ranking=scrapy.Field()
    # 电影名字
    title = scrapy.Field()
    # 参演明星
    star= scrapy.Field()
    # 上映时间
    releasetime= scrapy.Field()
    # 评分
    score= scrapy.Field()

    pass
