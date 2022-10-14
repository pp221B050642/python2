import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()
# cursor.execute("CREATE TABLE tkinter_users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, user_name VARCHAR(255) , password VARCHAR(255))")

# query = "INSERT INTO tkinter_users (user_name, password) VALUES (%s, %s)"

# values = [
#     ("adel", "abcde"),
#     ("philip", "azsxdcfv"),
#     ("george", "smith")]

# cursor.executemany(query, values)

# ## defining the Query
# query = "SELECT * FROM tkinter_users"
# ## getting records from the table
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()
# ## Showing the data
# for record in records:
#     print(record)

# db.commit()
