# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class SunproPipeline:
    def process_item(self, item, spider):
        return item
class MySQLPipline:
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='106.13.1.144',port=3306,user='database1',password='admin',database='database1',charset='utf8',ssl={'ssl':{}})

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            if item.__class__.__name__ == 'DetailItem':
                number1 = item['number']
                mysql_text_1 = f"select count(*) from sun where number = '{number1}'"
                print(mysql_text_1)
                self.cursor.execute(mysql_text_1)
                result = self.cursor.fetchall()
                result = list(result)[0]
                result = list(result)[0]
                if result > 0:
                    number1 = item['number']
                    detail_desc1 = item['detail_desc']
                    mysql_text_3 = f"update sun set detail_desc = '{detail_desc1}' where number = '{number1}'"
                    print(mysql_text_3)
                    self.cursor.execute(mysql_text_3)
                    self.conn.commit()
                else:
                    number1 = item['number']
                    detail_desc1 = item['detail_desc']
                    mysql_text_2 = f"insert into sun (number,detail_desc) values('{number1}','{detail_desc1}')"
                    print(mysql_text_2)
                    self.cursor.execute(mysql_text_2)
                    self.conn.commit()
            elif item.__class__.__name__ == 'SunproItem':
                number1 = item['number']
                mysql_text_1 = f"select count(*) from sun where number = '{number1}'"
                print(mysql_text_1)
                self.cursor.execute(mysql_text_1)
                result = self.cursor.fetchall()
                result = list(result)[0]
                result = list(result)[0]
                if result > 0:
                    number1 = item['number']
                    title1 = item['title']
                    link1 = item['link']
                    mysql_text_5 = f"update sun set title = '{title1}',link = '{link1}' where number = '{number1}'"
                    print(mysql_text_5)
                    self.cursor.execute(mysql_text_5)
                    self.conn.commit()
                else:
                    number1 = item['number']
                    title1 = item['title']
                    link1 = item['link']
                    mysql_text_4 = f"insert into sun (number,title,link) values('{number1}','{title1}','{link1}')"
                    print(mysql_text_4)
                    self.cursor.execute(mysql_text_4)
                    self.conn.commit()


        except Exception as e:
            print(f'submit mySQL error {e}')
            self.conn.rollback()
        return item
    def close_spider(self,spider):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as e:
            print(e)