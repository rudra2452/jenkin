import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
x=mysql.cursor()
name=input("Enter the Student name:")
sql="DELETE FROM student WHERE st_name= %s"
try:
    x.execute(sql,(name,))
    mysql.commit()
    print("Data deleted with the name", name)
except:
    print("Please check the entered data again")
finally:
    x.close()
    mysql.close()

