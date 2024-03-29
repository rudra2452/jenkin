import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
x=mysql.cursor()

st_name=input("Enter name of the stundent:- ")
try:
 sql=("SELECT * FROM student WHERE st_name LIKE %s")
 x.execute(sql,('%'+st_name+'%',))
 data=x.fetchall()
 print("Id, Name,Class,Email")
 print("---------------------------------")
 if data:
    for row in data:
       print(row)
 else:
       print("No Student found with this name, please recheck entered data")
 
except:
    print("Please recheck the entered name--")