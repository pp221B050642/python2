import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()

# cursor.execute("create table university (University_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, University_name VARCHAR(255), Students_count INT(11))")
# cursor.execute("create table professor (prof_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, prof_name VARCHAR(255), Uni_id INT(11), Joining_date DATE, Speciality VARCHAR(255), Salary VARCHAR(255), Experience INT(11))")
# cursor.execute("ALTER TABLE professor AUTO_INCREMENT = 101")
# query1 = "INSERT INTO university (University_name, Students_count) VALUES (%s, %s)"
# ## storing values in a variabl
# values = [
#     ('KBTU',1230),
#     ('KazNU', 10500 ),
#     ('KIMEP', 800),
#     ('ATU', 958)
# ]
# ## executing the query with values
# cursor.executemany(query1, values)
# ## to make final output we have to run the 'commit()' method of the database object
# db.commit()
# print(cursor.rowcount, "records inserted")

# query1 = "INSERT INTO professor (Prof_name, Uni_id, Joining_date, Speciality, Salary) VALUES (%s, %s, %s, %s, %s)"
# ## storing values in a variabl
# values = [
#     ("Zedan", 1, "2005-02-10", "Math", 3000),
#     ("Bekham", 1, "2010-08-30", "Physics", 3200),
#     ("Messi", 3, "2009-05-17", "Chemistry", 4000),
#     ("Habib", 3, "2006-11-11", "Math", 5000),
#     ("Ronaldo", 2, "2014-12-07", "History", 1000),
#     ("Neimar", 2, "2011-04-23", "Chemistry", 1500),
#     ("Silva", 4, "2020-09-01", "Baking", 800)
# ]
# ## executing the query with values
# cursor.executemany(query1, values)
# ## to make final output we have to run the 'commit()' method of the database object
# db.commit()
# print(cursor.rowcount, "records inserted")


# query = "SELECT * from professor"
# cursor.execute(query)
# l = cursor.fetchall()
# for i in l:
#     print(i)

