'''
DB연결을 위해 사용할 파일...?
이 패키지에서 CRUD를 쉽게 하기 위해 사용할 예정
사용할 db= mariaDB
'''

import pymysql as pysql
import pyodbc
import pandas as pd


server= ''

conn=None
cur=None
# sql=""
conn=pysql.connect(host='localhost',user='root',password='taegi',db='bms',charset='utf8')
cur= conn.cursor()

def createsql(sql):
    print("테스트")

def readsql(sql):
    cur.execute(sql)
    result=cur.fetchall()
    
    conn.commit()
    return result
