# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BossproPipeline:
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
            job_name = item["job_name"]
            salary = item["salary"]
            company = item["company"]
            workplace = item["workplace"]
            labels = item["labels"]
            hr_name = item["hr_name"]
            detail_url = item["detail_url"]
            job_desc = item["job_desc"]
            # print(job_name,salary,company,workplace,labels,hr_name,detail_url,job_desc)
            mysql_text = f"insert into boss (job_name,salary,company,workplace,labels,hr_name,detail_url,job_desc) values('{job_name}','{salary}','{company}','{workplace}','{labels}','{hr_name}','{detail_url}','{job_desc}')"
            print(f'insert into boss {company}')
            self.cursor.execute(mysql_text)
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