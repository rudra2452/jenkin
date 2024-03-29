import sqlite3
from turtle import update
conn=sqlite3.connect('customer.db')
#c=conn.execute('''create table customer(firstname test,lastname text, email teXt)''')
c=conn.cursor()
#many_customers=[('Munna','Kumar','muuna@gmail.com'), ('Niku','Singh','niku@outlook.com'),('sparsh','singh','sparsh@gmail.com')]
#c.execute("SELECT rowid,* FROM customer WHERE firstname='sparsh'")
# c.execute("""UPDATE customer SET email='munna@gmail.com' WHERE email='muuna@gmail.com'""")
# c.execute("""UPDATE customer SET lastname='Singh' WHERE lastname='Prakash'""")
# c.execute("""UPDATE customer SET lastname='Prakash' WHERE lastname='Singh'""")
# c.execute("""DELETE FROM customer WHERE firstname='Munna'""")
# c.execute("""SELECT rowid,* FROM customer ORDER BY rowid DESC""")
# c.execute("""SELECT rowid,* FROM customer LIMIT 2""")
c.execute("""SELECT rowid,* FROM customer WHERE firstname='Prem' AND lastname='Prakash'""")
conn.commit()
items=c.fetchall()
for item in items:
    print("Primay key-->", item[0])
    print("First name-->",item[1])
    print("Last name-->", item[2])
    # print("Email-->",item[3])
    print("-------------------------------------")
          

#print(c.fetchall())
#conn.executemany('''INSERT INTO customer VALUES(?,?,?)''',many_customers)
#conn.commit()
conn.close()