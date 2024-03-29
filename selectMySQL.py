import pymysql as mq

mysql=mq.connect(host="localhost",user="root",password="",database="school")
mycursor=mysql.cursor()
# print("{:>2} {:>2} {:>2} {:>5}".format("st_id","st_name", "st_class","st_email"))

print("{:>2} {:>2}".format("st_name", "st_class"))
print("--------------------")
try:
    sql="SELECT st_name,st_class FROM student"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for row in sdata:
        
        print(row)
        print("--------------------")
    
    # for s in sdata:
    #     print("{:>10},{:>30},{:>50},{:>5}.format (s[0],s[1],s[3])")
except:
    print("Error, check your inputes")

