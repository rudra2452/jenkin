import pymysql as mq
# try:
conn=mq.connect(host="localhost", user="root", password="", database= "learn")
mysql=conn.cursor()
id=input("Enter the state_id:-")
st_name=input("Enter the state name:-")
st_country=input("Enter the country name recpected to the state:-")
sql= "INSERT INTO state (id,st_name,st_country) VALUES(%s,%s,%s)"
data=(id,st_name,st_country)
# try:
mysql.execute(sql,data)
    
print("Data updated succesfully to the table named:-state")
    # st= "CREATE TABLE state(id INT PRIMARY KEY,st_name VARCHAR(10),st_country VARCHAR(15));"
    # mysql.execute(st)
print("Table updated:-state ")
conn.commit()

    # cnt="CREATE TABLE country(id INT PRIMARY KEY,ct_name VARCHAR(10),ct_rank VARCHAR(10));"
    # mysql.execute(cnt)
mysql_c=conn.cursor()
id=input("Enter the country id:-")
ct_name=input("Enter the name of the country:-")
ct_rank=input("Enter the rank of the country:-")
sql1="INSERT INTO country (id,ct_name,ct_rank) VALUES (%s,%s,%s)"
data1=(id,ct_name,ct_rank)
mysql_c.execute(sql1,data1)
print("Table created:-country")
conn.commit()
# except:
    # print("Table is already created")
    # print("Please check the code")



