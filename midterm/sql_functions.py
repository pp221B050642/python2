import mysql.connector as mysql
import datetime
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor(buffered=True)

def registration():
    user_name = input()
    user_password = input()
    phone_number = input()
    names = 'select user_name from visitors'
    cursor.execute(names)
    n = cursor.fetchall()
    if (user_name,) in n:
        print("user already exits")
    else:
        query = f"insert into visitors (user_name, passw, phone_number) values ('{user_name}', '{user_password}', '{phone_number}')"
        cursor.execute(query)
        db.commit()

def sign_in():
    user_name = input()
    user_password = input()
    names = "select user_name from visitors"
    cursor.execute(names)
    n = cursor.fetchall()
    passw = f"select passw from visitors where user_name = '{user_name}'"
    cursor.execute(passw)
    p = cursor.fetchall()
    if (user_name,) in n:
        if (user_password,) in p:
            print("welcome")
        else:
            print("password is not correct")
    else:
        print("user not found")

# not ready
def reservation():
    name = input()
    date_in = input("enter date in in this format yyyy-mm-dd: ")
    date_out = input("enter date out in this format yyyy-mm-dd: ")
    room_type = input()
    roomid = f"select id from rooms where room_type = '{room_type}'"
    cursor.execute(roomid)
    roomid2 = cursor.fetchall()
    visitorid = f"select id from visitors where user_name = '{name}'"
    cursor.execute(visitorid)
    visitor_id = cursor.fetchall()
    if len(roomid2)+5>0:
        room_id = roomid2[0][0]
    else:
        print(f"all {room_type} rooms are booked")

    black_list = f"select black_list from visitors where id = {visitor_id[0][0]}"
    cursor.execute(black_list)
    bl = cursor.fetchall()
    
    if (1, ) in bl:
        print(
        """You are in black list, 
so from your card would be deducted the full amount""")
    
    

    # query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"

    # cursor.execute(query)
    # db.commit()

def check_out():
    # room_id = f"select id from rooms where name_of_visitor = '{name}'"
    # cursor.execute(room_id)
    # id = cursor.fetchall()
    user_name = input()
    user_password = input()
    names = "select user_name from visitors"
    cursor.execute(names)
    n = cursor.fetchall()
    passw = f"select passw from visitors where user_name = '{user_name}'"
    cursor.execute(passw)
    p = cursor.fetchall()
    if (user_name,) in n:
        if (user_password,) in p:
            update_room = f"update rooms set name_of_visitor = NULL, check_in = NULL, check_out = NULL where name_of_visitor = '{user_name}'"
            cursor.execute(update_room)
            db.commit()
        else:
            print("password is not correct")
    else:
        print("user not found")
    
def cancel():
    name = input()
    cancel = 1
    cancels = f"select num_of_cancels from visitors where user_name = '{name}'"
    cursor.execute(cancels)
    c = cursor.fetchall()
    cancels2 = c[0][0]
    update_cancels = f"update visitors set num_of_cancels = {cancels2 + cancel} where user_name = '{name}'"
    cursor.execute(update_cancels)

    visitor_id = f"select id from visitors where user_name = '{name}'"
    cursor.execute(visitor_id)
    id = cursor.fetchall()

    roomid = f"select room_id from reservation where visitor_id = {id[0][0]}"
    cursor.execute(roomid)
    room_id = cursor.fetchall()

    checkin_date = f"select check_in from reservation where visitor_id = {id[0][0]}"
    cursor.execute(checkin_date)
    check_in_date = cursor.fetchall()
    now = datetime.date.today()  

    if cancels2+1>2:
        update_black_list = f"update visitors set black_list = 1 where user_name = '{name}'"
        cursor.execute(update_black_list)
    
    diff = check_in_date[0][0] - now
    diff_in_hours = diff.total_seconds() / 3600
    if diff_in_hours >= 12:
        update_table_reservation = f"delete from reservation where visitor_id = {id[0][0]}"
        cursor.execute(update_table_reservation)

        update_table_room = f"update rooms set status = 'vacant' where id = {room_id[0][0]}"
        cursor.execute(update_table_room)
        db.commit()
    else: 
        print("you cannot cancel your booking")

reservation()

