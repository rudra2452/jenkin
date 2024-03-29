from select import select
import pymysql as mq
conn=mq.connect(host="localhost", user="root", password="", database= "learn")
mysql=conn.cursor()
sql= "SELECT * FROM state INNER JOIN country on state.id=country.id"
mysql.execute(sql)
data=mysql.fetchall()
for x in data:
    print("{:<10} {:<15} {:<15} {:<15} {:<15}".format(x[0],x[1],x[2],x[3],x[4]))