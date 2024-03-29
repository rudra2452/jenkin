from ast import Try
import pymysql as mq
myobj = mq.connect(host="localhost", user="root", passwd="")
cursorobj=myobj.cursor()
try:
    db="create database school"
    cursorobj.execute(db)
    print("Database created")
except:
    print("Database error..")