import sqlite3

# Connect to the 'student.db' database
conn_student = sqlite3.connect('student.db')
c_student = conn_student.cursor()

# Connect to the 'fees.db' database
conn_fees = sqlite3.connect('fees.db')
c_fees = conn_fees.cursor()

# Define the SQL query to select data from 'fees' and 'student' tables using an inner join
sql_query = '''
SELECT *
FROM fees AS f
INNER JOIN student AS s ON f.st_id = s.st_id
'''

# Execute the SQL query
c_fees.execute(sql_query)

# Fetch all the rows from the result set
data = c_fees.fetchall()

# Print the fetched data
for row in data:
    print(row)
    print("------------------------------")

# Close the cursors and connections
c_student.close()
conn_student.close()

c_fees.close()
conn_fees.close()
