#-*- coding:utf-8 -*-
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#创建 dd_name 表
cursor.execute('DROP TABLE IF EXISTS dd_name')
cursor.execute('create table dd_name(xs_name VARCHAR (255) DEFAULT NULL ,xs_author VARCHAR (255),category VARCHAR (255),name_id VARCHAR (255))')
#创建 dd_chaptername 表
cursor.execute('DROP TABLE IF EXISTS dd_chaptername')
cursor.execute('''CREATE TABLE dd_chaptername(xs_chaptername VARCHAR(255) DEFAULT NULL ,xs_content TEXT,id_name INT(11) DEFAULT NULL,
                                                num_id INT(11) DEFAULT NULL ,url VARCHAR(255))''')
class Sql:
    #插入数据
    @classmethod
    def insert_dd_name(cls,xs_name,xs_author,category,name_id):
        # sql = "insert into dd_name (xs_name,xs_author,category,name_id) values (%(xs_name)s , %(xs_author)s , %(category)s , %(name_id)s)"
        sql = "insert into dd_name (xs_name,xs_author,category,name_id) values ('%s','%s','%s','%s')" % (xs_name,xs_author,category,name_id)
        cursor.execute(sql)
        conn.commit()
    #查重
    @classmethod
    def select_name(cls,name_id):
        sql = "SELECT EXISTS (select 1 from dd_name where name_id = '%s')" % name_id
        cursor.execute(sql)
        return cursor.fetchall()[0]


    @classmethod
    def insert_dd_chaptername(cls,xs_chaptername,xs_content,id_name,num_id,url):
        sql = '''INSERT INTO dd_chaptername(xs_chaptername , xs_content , id_name ,num_id ,
                url) VALUES ('%s' ,'%s' ,%s ,%s ,'%s')''' % (xs_chaptername,xs_content,id_name,num_id,url)

        cursor.execute(sql)
        conn.commit()

    @classmethod
    def select_chapter(cls,url):
        sql = "SELECT EXISTS (select 1 from dd_chaptername where url = '%s')" % url
        cursor.execute(sql)
        return cursor.fetchall()[0]
