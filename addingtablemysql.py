import pymysql as mq
mysql=mq.connect(host= "localhost", user= "root", password= "", database= "school")
mycursor=mysql.cursor()
try:
    ins= "INSERT INTO student(st_name,st_class,st_email) values(%s,%s,%s)"
    # t=[('raj','10th','raj@gmail.com'),('testing', '10th', 'testing@gmail.com')]
    t=[('delhi','10th','delhi@gmail.com'),('agiaon', '10th', 'agiaon@gmail.com')]
    mycursor.executemany(ins,t)
    mysql.commit();
    print("insert Data")
except:
    print("Error...")

    

