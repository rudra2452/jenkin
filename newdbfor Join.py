import pymysql as mq
myobj = mq.connect(host="localhost",user="root",password="")
c = myobj.cursor()
try:
   db="CREATE DATABASE learn"
   c.execute(db)
   print("Data base created with the name learn")
except:
   print("Error found..")
