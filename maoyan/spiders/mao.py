import scrapy
from scrapy.http import HtmlResponse
from scrapy import Request
from maoyan.items import MaoyanItem

class MaoSpider(scrapy.Spider):
    name = "mao"
    allowed_domains = ["maoyan.com"]
    # 确定爬取域名
    # start_urls = ["https://www.maoyan.com"]
    start_urls = []
    for page in range(0, 100, 10):
           start_urls.append(f'https://www.maoyan.com/board/4?timeStamp=1693882173594&channelId=40011&index=6&signKey=409374de54b869263f0a030792bafead&sVersion=1&webdriver=false&offset={page}')

    

    def parse(self, response:HtmlResponse):
        # 获取到Xpath定位
        list_neirong=response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        # //*[@id="app"]/div/div/div[1]/dl/dd[2]
        # print(list_neirong)
        for neirong in list_neirong:
            item=MaoyanItem()
            

            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/i
            item['ranking']=neirong.xpath('./i/text()').extract()[0]
            


            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/a
            item['title']=neirong.xpath('./div/div/div[1]/p[1]/a/@title').extract()[0]


            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[2]
            item['star']=neirong.xpath('normalize-space(./div/div/div[1]/p[2]/text())').extract()[0].replace("\n","")

            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[1]/p[3]
            item['releasetime']=neirong.xpath('./div/div/div[1]/p[3]/text()').extract()[0]

            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[1]
            # //*[@id="app"]/div/div/div[1]/dl/dd[1]/div/div/div[2]/p/i[2]
            item['score']=str(neirong.xpath('./div/div/div[2]/p/i[1]/text()').extract()[0])+str(neirong.xpath('./div/div/div[2]/p/i[2]/text()').extract()[0])
            yield item
