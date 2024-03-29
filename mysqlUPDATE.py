import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="",database="school")
x=mysql.cursor()
st_name=input("Enter the Student's name:-")
st_class=input("Enter the student's class:-")
st_email=input("Enter the email id:-")
st_id=input("Enter the Id:-")
sql=" UPDATE student SET st_name=%s,st_class=%s,st_email=%s WHERE st_id=%s"
data=(st_name,st_class,st_email,st_id)
# data= ("test singh","7th","test@gmail.com","4")
try:
    x.execute(sql,data)
    mysql.commit()
    print("Data updated", data)
except:
    print("Please check entered value")
    x.close()
    mysql.close()