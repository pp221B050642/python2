import mysql.connector as mysql
import datetime
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor(buffered=True)

def reservation():
    name = input()
    date_in = input("enter date in in this format yyyy-mm-dd: ")
    date_out = input("enter date out in this format yyyy-mm-dd: ")
    room_type = input()
    datein = datetime.datetime.strptime(date_in, '%Y-%m-%d')
    date_in = datetime.date.strftime(datein, "%Y-%m-%d")
    dateout = datetime.datetime.strptime(date_out, '%Y-%m-%d')

    dates = "select room_id, check_in, check_out from reservation"
    cursor.execute(dates)
    dates2 = cursor.fetchall()

    visitorid = f"select id from visitors where user_name = '{name}'"
    cursor.execute(visitorid)
    visitor_id = cursor.fetchall()

    roomid = f"select id from rooms where room_type = '{room_type}'"
    cursor.execute(roomid)
    roomid2 = cursor.fetchall()


    for i in range(len(dates2)):
        checkin = datetime.datetime.strftime(dates2[i][1], "%Y-%m-%d")
        checkout = datetime.datetime.strftime(dates2[i][2], "%Y-%m-%d")
        check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d')
        check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d')
        # print((dates2[i][0],) )
        if check_in<=datein<=check_out or datein<=check_in<=dateout:
            print(dates2[i])
            if (dates2[i][0], ) in roomid2:
                roomid2.remove((dates2[i][0],))
    
    if len(roomid2)>0:
        room_id = roomid2[0][0]
        query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
        cursor.execute(query)
        db.commit()
    else:
        print(f"all {room_type} rooms are booked")




reservation()

    


    
    # roomidinreservation = f"select room_id from reservation"
    # cursor.execute(roomidinreservation)
    # roomidreservation = cursor.fetchall()
    # print(roomidreservation)

    # reserv = {}
    # for i in range(len(dates2)):
    #     reserv[dates2[i][0]] = [dates2[i][1], dates2[i][2]]

    # if (room_id,) in roomidreservation:

    #     pass

    # for i in roomid2:
    #     if i in roomidreservation:
    #         date1 = f"select check_in, check_out from reservation where room_id = '{i[0]}'"
    #         cursor.execute(date1)
    #         date2=cursor.fetchall()
    #         for i in date2:
    #             if date_in>i[0] and date_in<i[1]:
    #                 print(i)
    #     else:
    #         pass
            # if len(roomid2)>0:
            #     room_id = roomid2[0][0]
            #     query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
            #     query2 = f"update rooms set status = '{nvacant}' where id = {room_id}"
            #     cursor.execute(query)
            #     cursor.execute(query2)
            #     db.commit()
            # else:
            #     print(f"all {room_type} rooms are booked")


