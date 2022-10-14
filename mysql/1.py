import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()

# ## defining the Query
# query = "UPDATE users SET name = 'Kareem' WHERE id = 1"
# ## executing the query
# cursor.execute(query)
# ## final step to tell the database that we have changed the table data
# db.commit()


# ## defining the Query
# query = "SELECT * FROM users"
# ## getting records from the table
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()
# ## Showing the data
# for record in records:
#     print(record)


# ## defining the Query
# query = "DELETE FROM users WHERE id = 5"
# ## executing the query
# cursor.execute(query)
# ## final step to tell the database that we have changed the table data
# db.commit()


# ## defining the Query
# query = "SELECT * FROM users ORDER BY name" #in descending order "SELECT * FROM users ORDER BY name DESC"
# ## getting records from the table
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()
# ## Showing the data
# for record in records:
#     print(record)



# ## defining the Query
# query = "SELECT * FROM users WHERE id = 5"
# ## getting records from the table
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()
# ## Showing the data
# for record in records:
#     print(record)


# ## defining the Query
# query = "SELECT user_name FROM users" # we cal also select more than one column"SELECT name, user_name FROM users"
# ## getting 'user_name' column from the table
# cursor.execute(query)
# ## fetching all usernames from the 'cursor' object
# usernames = cursor.fetchall()
# ## Showing the data
# for username in usernames:
#     print(username)


# ## defining the Query
# query = "SELECT * FROM users"
# ## getting records from the table
# cursor.execute(query)
# ## fetching all records from the 'cursor' object
# records = cursor.fetchall()
# ## Showing the data
# for record in records:
#     print(record)


# ## defining the Query
# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# ## storing values in a variable
# values = [
#     ("Peter", "peter"),
#     ("Amy", "amy"),
#     ("Michael", "michael"),
#     ("Hennah", "hennah")]
# ## executing the query with values
# cursor.executemany(query, values)
# ## to make final output we have to run the 'commit()' method of the database object
# db.commit()
# print(cursor.rowcount, "records inserted")


# ## defining the Query
# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# ## storing values in a variable
# values = ("Hafeez", "hafeez")
# ## executing the query with values
# cursor.execute(query, values)
# ## to make final output we have to run the 'commit()' method of the database object
# db.commit()
# print(cursor.rowcount, "record inserted")


## adding 'id' column to the 'users' table
## 'FIRST' keyword in the statement will add a column in the starting of the table
# cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

## dropping the 'id' column
# cursor.execute("ALTER TABLE users DROP id")

## 'DESC table_name' is used to get all columns information
# cursor.execute("DESC users")
# print(cursor.fetchall())

## creating the 'users' table again with the 'PRIMARY KEY'
# cursor.execute("DROP TABLE users")
# cursor.execute("CREATE TABLE users (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# for table in tables:
#     print(table)

# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")

# cursor.execute("CREATE DATABASE test")

# cursor.execute("SHOW DATABASES")
# databases = cursor.fetchall()
# print(databases)
# for database in databases:
#     print(database)
