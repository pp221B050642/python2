import mysql.connector as mysql
import datetime
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor(buffered=True)


room = 'econom'
oprice = f"select price from rooms where room_type = '{room}'"
cursor.execute(oprice)
pprice = cursor.fetchall()
ppprice = pprice[0][0]

print(ppprice)
# roomid = f"select id from rooms where room_type = ''"
# cursor.execute(roomid)
# roomid2 = cursor.fetchall()
# visitorid = f"select id from visitors where user_name = ''"
# cursor.execute(visitorid)
# visitor_id = cursor.fetchall()
