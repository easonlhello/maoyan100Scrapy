# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import openpyxl
import pymysql

# ranking,title,star,releasetime,score
class DBMaoyanPipeline:
     def __init__(self) :
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            database='maoyan',
            charset='utf8mb4'
        )
        self.cursor = self.conn.cursor()
     def close_spider(self,spider):
        self.conn.commit()
        self.conn.close()
        print('导入成功')
     def process_item(self, item, spider):
        title = item.get('title', '')
        ranking = item.get('ranking', '')
        star = item.get('star', '')
        releasetime = item.get('releasetime', '')
        score = item.get('score', '')

        self.cursor.execute(
            'insert into maoyanshuju(ranking,title,star,releasetime,score) values (%s,%s,%s,%s,%s,)',
            (ranking,title,star,releasetime,score)
        )
        # 以便后续获取到item
        return item




class MaoyanPipeline:
    # 初始化
    def __init__(self) :
        self.wb= openpyxl.Workbook()
        self.ws=self.wb.active
        self.ws.title='猫眼100'
        self.ws.append(('ranking','title','star','releasetime','score'))
    # 关闭
    def close_spider(self,spider):
        self.wb.save('猫眼100.xlsx')

    def process_item(self, item, spider):
        title = item.get('title', '')
        ranking = item.get('ranking', '')
        star = item.get('star', '')
        releasetime = item.get('releasetime', '')
        score = item.get('score', '')
        self.ws.append((ranking,title,star,releasetime,score))

        return item
    # connect mysql
    # def __init__(self):
    #     self.conn = pymysql.connect(
    #         host='127.0.0.1',
    #         port=3306,
    #         user='root',
    #         password='root',
    #         database='maoyan',
    #         charset='utf8mb4'
    #     )
    #     self.cursor = self.conn.cursor()

    # def close_spider(self, spider):
    #     self.conn.commit()
    #     self.conn.close()
    #     print('导入成功')

    # def process_item(self, item, spider):
    #     # anking,title,star,releasetime,score
    #     title = item.get('title', '')
    #     ranking = item.get('ranking', '')
    #     star = item.get('star', '')
    #     releasetime = item.get('releasetime', '')
    #     score = item.get('score', '')

    #     self.cursor.execute(
    #         'insert into maoyanshuju(ranking,title,star,releasetime,score) values (%s,%s,%s,%s,%s,)',
    #         (ranking,title,star,releasetime,score)
    #     )
    #     # 以便后续获取到item
        # return item
