import sqlite3

conn_fees=sqlite3.connect('fees.db')
c_fees=conn_fees.cursor()
c_fees.execute("""UPDATE fees SET fees_amount='4000' WHERE fees_amount='5000'""")
conn_fees.commit()



# conn_student=sqlite3.connect('student.db')
# c_student=conn_student.cursor()




# c=('''SELECT * FROM  fees''') #AS f INNER JOIN student AS s on f.st_id = s.st_id''')
   
# c_fees.execute(c)
print(c_fees)
# data=c_fees.fetchall()
# for row in data:
#     print(row)
#     print("------------------------------")
