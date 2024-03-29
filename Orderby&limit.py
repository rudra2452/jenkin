import select
import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
x=mysql.cursor()

try:
    sql= "select * from student order by st_name ASC LIMIT 2,2"
    x.execute(sql)
    data=x.fetchall()
    for row in data:
        print(row)
    
except:
    print("Error...")

