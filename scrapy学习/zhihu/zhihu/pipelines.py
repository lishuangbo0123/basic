# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class ZhihuPipeline:
    f = None
    #重写父类的方法，该方法只在开始爬虫的时候调用一次
    def open_spider(self,spider):
        print("开始爬虫")
        self.f = open('zhihu.txt','w',encoding='utf-8')

    # 专门用来处理item,该方法可以接受爬虫文件提交过来的item对象
    #该方法每接受到一次item就会被掉用一次

    def process_item(self, item, spider):
        title = item['title']
        self.f.write(title)
        return item  #就会传递给下一个即将被执行的管道类
    #重写父类方法，结束爬虫只调用一次
    def close_spider(self,spider):
        print('结束爬虫')
        self.f.close()
# ALTER USER 'database1'@'106.13.1.144' IDENTIFIED WITH mysql_native_password BY 'a00000000'
class MySQLPipline:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='106.13.1.144',port=3306,user='database1',password='admin',database='database1',charset='utf8',ssl={'ssl':{}})

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(f'insert into zhihu values({item["title"]})')
            self.conn.commit()
            print('提交数据'+ item["title"])
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

#爬虫文件提交的item会给哪个管道类呢？   给优先级较高的管道类