import tkinter as tk
import datetime as datetime
import re
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()



def click_check_out_button():  #checking out function
    def check_entry():
        name=name_entry.get()
        password=password_entry.get()
        if name!="" and password!="":
            names = "select user_name from visitors"
            cursor.execute(names)
            n = cursor.fetchall()
            passw = f"select passw from visitors where user_name = '{name}'"
            cursor.execute(passw)
            p = cursor.fetchall()
            if (name,) in n:
                if (password,) in p:
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
                        def ok():
                                    success.destroy()
                                    checkout.destroy()
                        update_table_reservation = f"delete from reservation where visitor_id = {id[0][0]}"
                        cursor.execute(update_table_reservation)

                        db.commit()
                        success=tk.Tk()
                        success.title("success")
                        success.configure(bg="white")
                        success.geometry("200x50+750+300")
                        success_lab=tk.Label(success, text="your cancel is success", bg="white").place(x=0, y=0)
                        ok_button=tk.Button(success, text="ok", bg="white", command= ok).place(x=80, y=25)

                    else: 
                        error_window=tk.Tk()
                        error_window.title("error")
                        error_window.geometry("200x100+750+650")
                        error_lab=tk.Label(error_window, text="You cannot cancel your booking, because time for check in is less than 12 hours").pack()
                else:
                    error_window=tk.Tk()
                    error_window.title("error")
                    error_window.geometry("200x100+750+650")
                    error_lab=tk.Label(error_window, text="password is not correct(").pack()
            else:
                error_window=tk.Tk()
                error_window.title("error")
                error_window.geometry("200x100+750+650")
                error_lab=tk.Label(error_window, text="user is not found(").pack()
                print(name, password)
        else:
            error_lab=tk.Label(checkout, text="*fields can`t be empty", bg="white")
            error_lab.place(x=120, y=190)
        


    checkout=tk.Tk()
    checkout.title("cancelling")
    checkout.configure(bg="white")
    checkout.geometry("500x300+500+200")
    #checking out label
    checkout_lab=tk.Label(checkout, text="Hello! If you want to cancel, please, sign in first:", bg="white", font=("Pobeda",20))
    checkout_lab.place(x=10, y=50)
    password_entry=tk.Entry(checkout)
    password_entry.config(show="*")
    password_entry.place(x=120, y=150, width=350, height=40)
    name_entry=tk.Entry(checkout)
    name_entry.place(x=120, y=100, width=350, height=40)
    name_lab=tk.Label(checkout, text="Name: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=110)
    password_lab=tk.Label(checkout, text="Password: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=160)
    checkout_button=tk.Button(checkout,text="cancel", bg="white", font=("AC Boucle", 30), command=check_entry).place(x=120, y=210)

def click_reservation_button(): #reservation button
    def register():
        def check_entry():
            def result():
                room_type=var1.get()
                payment_method=var2.get()
                
                count=0
                year1=date1_year.get()
                month1=date1_month.get()
                day1=date1_day.get()
                year2=date2_year.get()
                month2=date2_month.get()
                day2=date2_day.get()
                print(year1)
                
                if year1=="" or year2=="" or month1=="" or month2=="" or day1=="" or day2=="": 
                    error=tk.Tk()
                    error.configure(bg="white")
                    error.title("error")
                    error.geometry("200x50+750+300")
                    error_lab=tk.Label(error, text="insert all the date data", bg="white")
                    error_lab.place(x=0, y=0)
                    
                else:
                    year1=int(year1)
                    year2=int(year2)
                    month1=int(month1)
                    month2=int(month2)
                    day1=int(day1)
                    day2=int(day2)
                    try:
                        date1 = datetime.date(year1, month1, day1)
                        date2 = datetime.date(year2, month2, day2)
                        now=datetime.date.today()
                        if date1<now or date2<now or date2<=date1:
                            error=tk.Tk()
                            error.configure(bg="white")
                            error.title("error")
                            error.geometry("200x50+750+300")
                            error_lab=tk.Label(error, text="Date is not correct", bg="white")
                            error_lab.place(x=0, y=0)
                        else:
                            count=1
                    except ValueError:
                        error=tk.Tk()
                        error.configure(bg="white")
                        error.title("error")
                        error.geometry("200x50+750+300")
                        error_lab=tk.Label(error, text="Month [1-12], date [1-31]", bg="white")
                        error_lab.place(x=0, y=0)

                    if payment_method==0 and count==1:
                        def check_validation():
                            cardnumber=card_number.get()

                            valid = r"\b(4|5|6)(\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4}\b)"

                            non_repeated = r'(\d)(-?\1){3}'

                            if re.findall(valid, cardnumber):
                                if re.findall(non_repeated, cardnumber):
                                    error=tk.Tk()
                                    error.configure(bg="white")
                                    error.title("error")
                                    error.geometry("200x50+750+300")
                                    error_lab=tk.Label(error, text="Card number is not valid!", bg="white")
                                    error_lab.place(x=0, y=0)
                                else:
                                    def ok():
                                        success.destroy()
                                    if room_type==0:
                                        room="econom"
                                    elif room_type==1:
                                        room="lux"
                                    else:
                                        room="presidential"
                                    date1 = datetime.date(year1, month1, day1)
                                    date2 = datetime.date(year2, month2, day2)
                                    oprice = f"select price from rooms where room_type = '{room}'"
                                    cursor.execute(oprice)
                                    pprice = cursor.fetchall()
                                    ppprice = pprice[0][0]
                                    validation.destroy()
                                    reservation.destroy()
                                    success=tk.Tk()
                                    success.title("success")
                                    success.configure(bg="white")
                                    success.geometry("250x75+750+300")
                                    check=(date2-date1).days
                                    
                                    price=ppprice*check
                                    success_lab=tk.Label(success, text=f"the price for one night = {ppprice}KZT\nthe total price = {price}KZT", bg="white").place(x=15, y=0)
                                    ok_button=tk.Button(success, text="ok", bg="white", command= ok).place(x=80, y=35)
                                    date_in=date1
                                    date_out=date2
                                    ###############
                                    
                                    datein = datetime.datetime.strftime(date_in, '%Y-%m-%d')
                                    date_in2 = datetime.datetime.strptime(datein, '%Y-%m-%d')
                                    dateout = datetime.datetime.strftime(date_out, '%Y-%m-%d')
                                    date_out2 = datetime.datetime.strptime(dateout, '%Y-%m-%d')
                                    

                                    dates = "select room_id, check_in, check_out from reservation"
                                    cursor.execute(dates)
                                    dates2 = cursor.fetchall()

                                    visitorid = f"select id from visitors where user_name = '{name}'"
                                    cursor.execute(visitorid)
                                    visitor_id = cursor.fetchall()

                                    roomid = f"select id from rooms where room_type = '{room}'"
                                    cursor.execute(roomid)
                                    roomid2 = cursor.fetchall()


                                    for i in range(len(dates2)):
                                        checkin = datetime.datetime.strftime(dates2[i][1], "%Y-%m-%d")
                                        checkout = datetime.datetime.strftime(dates2[i][2], "%Y-%m-%d")
                                        check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d')
                                        check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d')
                                        # print((dates2[i][0],) )
                                        if check_in<=date_in2<=check_out or date_in2<=check_in<=date_out2:
                                            if (dates2[i][0], ) in roomid2:
                                                roomid2.remove((dates2[i][0],))

                                    if len(roomid2)>0:
                                        room_id = roomid2[0][0]
                                        query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
                                        cursor.execute(query)
                                        db.commit()
                                    else:
                                        sad_window=tk.Tk()
                                        sad_window.title("sad info")
                                        sad_window.geometry("200x100+750+650")
                                        sad_lab=tk.Label(sad_window, text=f"Sorry, all {rooms} rooms are booked\nYou can try to search other rooms").pack()
                                        sad_window.mainloop()
                                    print(date_in, date_out, room_type)
                            else:
                                error=tk.Tk()
                                error.configure(bg="white")
                                error.title("error")
                                error.geometry("200x50+750+300")
                                error_lab=tk.Label(error, text="Card number is not valid!", bg="white")
                                error_lab.place(x=0, y=0)

                        validation=tk.Tk()
                        validation.title("validation")
                        validation.configure(bg="white")
                        validation.geometry("600x100+750+200")
                        card_label=tk.Label(validation, text="Please, write the card number:", bg="white").place(y=10)
                        card_number=tk.Entry(validation, bg="white")
                        card_number.place(y=30, width=400, height=30)
                        check_button=tk.Button(validation, bg="white", text="Check", command= check_validation).place(y=60)
                    elif payment_method==1 and count==1:
                        def ok():
                            success.destroy()
                        if room_type==0:
                            room="econom"
                        elif room_type==1:
                            room="lux"
                        else:
                            room="presidential"
                        date1 = datetime.date(year1, month1, day1)
                        date2 = datetime.date(year2, month2, day2)
                        oprice = f"select price from rooms where room_type = '{room}'"
                        cursor.execute(oprice)
                        pprice = cursor.fetchall()
                        ppprice = pprice[0][0]
                        reservation.destroy()
                        success=tk.Tk()
                        success.title("success")
                        success.configure(bg="white")
                        success.geometry("250x75+750+300")
                        check=(date2-date1).days
                        
                        price=ppprice*check
                        success_lab=tk.Label(success, text=f"the price for one night = {ppprice}KZT\nthe total price = {price}KZT", bg="white").place(x=15, y=0)
                        ok_button=tk.Button(success, text="ok", bg="white", command= ok).place(x=80, y=35)
                        date_in=date1
                        date_out=date2
                        ###############
                        

                        datein = datetime.datetime.strftime(date_in, '%Y-%m-%d')
                        date_in2 = datetime.datetime.strptime(datein, '%Y-%m-%d')
                        dateout = datetime.datetime.strftime(date_out, '%Y-%m-%d')
                        date_out2 = datetime.datetime.strptime(dateout, '%Y-%m-%d')

                        dates = "select room_id, check_in, check_out from reservation"
                        cursor.execute(dates)
                        dates2 = cursor.fetchall()

                        visitorid = f"select id from visitors where user_name = '{name}'"
                        cursor.execute(visitorid)
                        visitor_id = cursor.fetchall()

                        roomid = f"select id from rooms where room_type = '{room}'"
                        cursor.execute(roomid)
                        roomid2 = cursor.fetchall()


                        for i in range(len(dates2)):
                            checkin = datetime.datetime.strftime(dates2[i][1], "%Y-%m-%d")
                            checkout = datetime.datetime.strftime(dates2[i][2], "%Y-%m-%d")
                            check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d')
                            check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d')
                            # print((dates2[i][0],) )
                            if check_in<=date_in2<=check_out or date_in2<=check_in<=date_out2:
                                if (dates2[i][0], ) in roomid2:
                                    roomid2.remove((dates2[i][0],))

                        if len(roomid2)>0:
                            room_id = roomid2[0][0]
                            query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
                            cursor.execute(query)
                            db.commit()
                        else:
                            sad_window=tk.Tk()
                            sad_window.title("sad info")
                            sad_window.geometry("200x100+750+650")
                            sad_lab=tk.Label(sad_window, text=f"Sorry, all {rooms} rooms are booked\nYou can try to search other rooms").pack()
                            sad_window.mainloop()
                        print(date_in, date_out, room_type)
                        
            name=name_entry.get()
            number=number_entry.get()
            password=password_entry.get()
            pattern_phone="^[0-9]{11}$"
        
            if name!="" and number!="" and password!="":
                if re.findall(pattern_phone, number):
                    names = 'select user_name from visitors'
                    cursor.execute(names)
                    n = cursor.fetchall()
                    if (name,) in n:
                        error_window=tk.Tk()
                        error_window.geometry("100x400+750+650")
                        error_lab=tk.Label(error_window, text="user already exists, please try to sign in", bg="white").pack()
                        registration.destroy()
                    else:
                        query = f"insert into visitors (user_name, passw, phone_number) values ('{name}', '{password}', '{number}')"
                        cursor.execute(query)
                        db.commit()
                    registration.destroy()
                    #new window for reservation
                    reservation=tk.Tk()
                    reservation.configure(bg="white")
                    reservation.title("reservation")
                    reservation.geometry("600x250+500+200")
                    var1= tk.IntVar(reservation)
                    
                    var2=tk.IntVar(reservation)
                
                    #date fields
                    date1_year=tk.Entry(reservation)
                    date1_year.place(x=10, y=60, width=50, height=30)
                    date1_month=tk.Entry(reservation)
                    date1_month.place(x=70, y=60, width=30, height=30)
                    date1_day=tk.Entry(reservation)
                    date1_day.place(x=110, y=60, width=30, height=30)
                    date2_year=tk.Entry(reservation)
                    date2_year.place(x=10, y=120, width=50, height=30)
                    date2_month=tk.Entry(reservation)
                    date2_month.place(x=70, y=120, width=30, height=30)
                    date2_day=tk.Entry(reservation)
                    date2_day.place(x=110, y=120, width=30, height=30)
                    #labels for dates
                    date1_lab=tk.Label(reservation, text="Choose the arrival date (yy/mm/dd):", bg="white")
                    date1_lab.place(x=10, y=32)
                    date2_lab=tk.Label(reservation, text="Choose the arrival date (yy/mm/dd):", bg="white")
                    date2_lab.place(x=10, y=92)
                    #label for room type
                    room_type=tk.Label(reservation, text="room type:", bg="white")
                    room_type.place(x=290, y=45)
                    #label for payment
                    payment=tk.Label(reservation, text="payment method:", bg="white")
                    payment.place(x=430, y=60)
                    #tick buttons
                    econom_tick=tk.Radiobutton(reservation, text="econom",bg="white", variable=var1, value=0)
                    luxe_tick=tk.Radiobutton(reservation, text="luxe",bg="white",variable=var1, value=1)
                    president_tick=tk.Radiobutton(reservation, text="president",bg="white",variable=var1, value=2)
                    econom_tick.place(x=290, y=65)
                    luxe_tick.place(x=290, y=95)
                    president_tick.place(x=290, y=125)
                    #payment tick buttons
                    card=tk.Radiobutton(reservation, text="by card", bg="white", variable=var2, value=0)
                    cash=tk.Radiobutton(reservation, text="by cash", bg="white", variable=var2, value=1)
                    card.place(x=430, y=80)
                    cash.place(x=430, y=100)

                    reserve=tk.Button(reservation, text="reserve",bg="white", font=("AC Boucle", 20), command=result).place(x=240, y=180)
                else:
                    error_lab=tk.Label(registration, text="the number is wrong", bg="white")
                    error_lab.place(x=10, y=250)
            else:
                error_lab=tk.Label(registration, text="fields can`t be empty", bg="white")
                error_lab.place(x=10, y=250)
        choose.destroy()
        registration=tk.Tk()
        registration.configure(bg="white")
        registration.title("registration")
        registration.geometry("500x400+500+200")
        make_res=tk.Label(registration, text="Please, register first:", bg="white", font=("Pobeda", 20)).place(x=30, y=60)
        #name
        name_entry=tk.Entry(registration, text="name")
        name_entry.place(x=120, y=100, width=350, height=40)
        #number
        number_entry=tk.Entry(registration)
        number_entry.place(x=120, y=150, width=350, height=40)
        
        #password
        password_entry=tk.Entry(registration)
        password_entry.config(show="*")
        password_entry.place(x=120, y=200, width=350, height=40)
        #labels
        name_lab=tk.Label(registration, text="Name: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=110)
        number_lab=tk.Label(registration, text="Phone: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=160)
        password_lab=tk.Label(registration, text="Password: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=210)
        register_button=tk.Button(registration,text="registration",  bg="white", font=("AC Boucle", 30), command=check_entry).place(x=120, y=320)
    def sighin():
        def check_entry():
            def result():
                
                room_type=var1.get()
                payment_method=var2.get()
                
                count=0
                year1=date1_year.get()
                month1=date1_month.get()
                day1=date1_day.get()
                year2=date2_year.get()
                month2=date2_month.get()
                day2=date2_day.get()
                print(year1)
                
                if year1=="" or year2=="" or month1=="" or month2=="" or day1=="" or day2=="": 
                    error=tk.Tk()
                    error.configure(bg="white")
                    error.title("error")
                    error.geometry("200x50+750+300")
                    error_lab=tk.Label(error, text="insert all the date data", bg="white")
                    error_lab.place(x=0, y=0)
                    
                else:
                    year1=int(year1)
                    year2=int(year2)
                    month1=int(month1)
                    month2=int(month2)
                    day1=int(day1)
                    day2=int(day2)
                    try:
                        date1 = datetime.date(year1, month1, day1)
                        date2 = datetime.date(year2, month2, day2)
                        now=datetime.date.today()
                        if date1<now or date2<now or date2<=date1:
                            error=tk.Tk()
                            error.configure(bg="white")
                            error.title("error")
                            error.geometry("200x50+750+300")
                            error_lab=tk.Label(error, text="Date is not correct", bg="white")
                            error_lab.place(x=0, y=0)
                        else:
                            count=1
                    except ValueError:
                        error=tk.Tk()
                        error.configure(bg="white")
                        error.title("error")
                        error.geometry("200x50+750+300")
                        error_lab=tk.Label(error, text="Month [1-12], date [1-31]", bg="white")
                        error_lab.place(x=0, y=0)

                    if payment_method==0 and count==1:
                        
                        
                        visitorid = f"select id from visitors where user_name = '{name}'"
                        cursor.execute(visitorid)
                        visitor_id = cursor.fetchall()
                        black_list = f"select black_list from visitors where id = {visitor_id[0][0]}"
                        cursor.execute(black_list)
                        bl = cursor.fetchall()
                        def clear():
                            reservation.destroy()
                            warning.destroy()
                        def opening():
                            def check_validation():
                                cardnumber=card_number.get()

                                valid = r"\b(4|5|6)(\d{3})\-?(\d{4})\-?(\d{4})\-?(\d{4}\b)"

                                non_repeated = r'(\d)(-?\1){3}'

                                if re.findall(valid, cardnumber):
                                    if re.findall(non_repeated, cardnumber):
                                        error=tk.Tk()
                                        error.configure(bg="white")
                                        error.title("error")
                                        error.geometry("200x50+750+300")
                                        error_lab=tk.Label(error, text="Card number is not valid!", bg="white")
                                        error_lab.place(x=0, y=0)
                                    else:
                                        def ok():
                                            success.destroy()
                                        if room_type==0:
                                            room="econom"
                                        elif room_type==1:
                                            room="lux"
                                        else:
                                            room="presidential"
                                        date1 = datetime.date(year1, month1, day1)
                                        date2 = datetime.date(year2, month2, day2)
                                        oprice = f"select price from rooms where room_type = '{room}'"
                                        cursor.execute(oprice)
                                        pprice = cursor.fetchall()
                                        ppprice = pprice[0][0]
                                        validation.destroy()
                                        reservation.destroy()
                                        success=tk.Tk()
                                        success.title("success")
                                        success.configure(bg="white")
                                        success.geometry("250x75+750+300")
                                        check=(date2-date1).days
                                        
                                        price=ppprice*check
                                        success_lab=tk.Label(success, text=f"the price for one night = {ppprice}KZT\nthe total price = {price}KZT", bg="white").place(x=15, y=0)
                                        ok_button=tk.Button(success, text="ok", bg="white", command= ok).place(x=80, y=35)
                                        date_in=date1
                                        date_out=date2
                                        ###############
                                        
                                        datein = datetime.datetime.strftime(date_in, '%Y-%m-%d')
                                        date_in2 = datetime.datetime.strptime(datein, '%Y-%m-%d')
                                        dateout = datetime.datetime.strftime(date_out, '%Y-%m-%d')
                                        date_out2 = datetime.datetime.strptime(dateout, '%Y-%m-%d')

                                        dates = "select room_id, check_in, check_out from reservation"
                                        cursor.execute(dates)
                                        dates2 = cursor.fetchall()

                                        visitorid = f"select id from visitors where user_name = '{name}'"
                                        cursor.execute(visitorid)
                                        visitor_id = cursor.fetchall()

                                        roomid = f"select id from rooms where room_type = '{room}'"
                                        cursor.execute(roomid)
                                        roomid2 = cursor.fetchall()


                                        for i in range(len(dates2)):
                                            checkin = datetime.datetime.strftime(dates2[i][1], "%Y-%m-%d")
                                            checkout = datetime.datetime.strftime(dates2[i][2], "%Y-%m-%d")
                                            check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d')
                                            check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d')
                                            # print((dates2[i][0],) )
                                            if check_in<=date_in2<=check_out or date_in2<=check_in<=date_out2:
                                                if (dates2[i][0], ) in roomid2:
                                                    roomid2.remove((dates2[i][0],))

                                        if len(roomid2)>0:
                                            room_id = roomid2[0][0]
                                            query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
                                            cursor.execute(query)
                                            db.commit()
                                        else:
                                            sad_window=tk.Tk()
                                            sad_window.title("sad info")
                                            sad_window.geometry("200x100+750+650")
                                            sad_lab=tk.Label(sad_window, text=f"Sorry, all {rooms} rooms are booked\nYou can try to search other rooms").pack()
                                            sad_window.mainloop()
                                else:
                                    error=tk.Tk()
                                    error.configure(bg="white")
                                    error.title("error")
                                    error.geometry("200x50+750+300")
                                    error_lab=tk.Label(error, text="Card number is not valid!", bg="white")
                                    error_lab.place(x=0, y=0)
                            
                            validation=tk.Tk()
                            validation.title("validation")
                            validation.configure(bg="white")
                            validation.geometry("600x100+750+200")
                            card_label=tk.Label(validation, text="Please, write the card number:", bg="white").place(y=10)
                            card_number=tk.Entry(validation, bg="white")
                            card_number.place(y=30, width=400, height=30)
                            check_button=tk.Button(validation, bg="white", text="Check", command= check_validation).place(y=60)
                        if (1, ) in bl:######################################
                            
                            warning=tk.Tk()
                            warning.configure(bg="white")
                            warning.title("warning")
                            warning.geometry("300x100+750+300")
                            warning_lab=tk.Label(warning, text='You are in black list,\nso from your card would be deducted the full amount', bg="white")
                            warning_lab.place(x=10, y = 10)
                            ok = tk.Button(warning, text="ok", bg="white", command= opening).place(x=100, y=40) 
                            not_ok = tk.Button(warning, text="not ok", bg="white", command=clear).place(x=150, y=40)
                            warning_lab.place(x=0, y=0)
                        else:
                            opening()
                        
                    elif payment_method==1 and count==1:
                        
                        visitorid = f"select id from visitors where user_name = '{name}'"
                        cursor.execute(visitorid)
                        visitor_id = cursor.fetchall()
                        black_list = f"select black_list from visitors where id = {visitor_id[0][0]}"
                        cursor.execute(black_list)
                        bl = cursor.fetchall()
                        
                        def clear():
                            reservation.destroy()
                            warning.destroy()
                        
                        def opening():
                            def ok():
                                success.destroy()
                            if room_type==0:
                                room="econom"
                            elif room_type==1:
                                room="lux"
                            else:
                                room="presidential"
                            date1 = datetime.date(year1, month1, day1)
                            date2 = datetime.date(year2, month2, day2)
                            oprice = f"select price from rooms where room_type = '{room}'"
                            cursor.execute(oprice)
                            pprice = cursor.fetchall()
                            ppprice = pprice[0][0]

                            reservation.destroy()
                            success=tk.Tk()
                            success.title("success")
                            success.configure(bg="white")
                            success.geometry("250x75+750+300")
                            check=(date2-date1).days

                            price=ppprice*check
                            success_lab=tk.Label(success, text=f"the price for one night = {ppprice}KZT\nthe total price = {price}KZT", bg="white").place(x=15, y=0)
                            ok_button=tk.Button(success, text="ok", bg="white", command= ok).place(x=80, y=35)
                            date_in=date1
                            date_out=date2
                            ###############


                            datein = datetime.datetime.strftime(date_in, '%Y-%m-%d')
                            date_in2 = datetime.datetime.strptime(datein, '%Y-%m-%d')
                            dateout = datetime.datetime.strftime(date_out, '%Y-%m-%d')
                            date_out2 = datetime.datetime.strptime(dateout, '%Y-%m-%d')

                            dates = "select room_id, check_in, check_out from reservation"
                            cursor.execute(dates)
                            dates2 = cursor.fetchall()

                            visitorid = f"select id from visitors where user_name = '{name}'"
                            cursor.execute(visitorid)
                            visitor_id = cursor.fetchall()

                            roomid = f"select id from rooms where room_type = '{room}'"
                            cursor.execute(roomid)
                            roomid2 = cursor.fetchall()


                            for i in range(len(dates2)):
                                checkin = datetime.datetime.strftime(dates2[i][1], "%Y-%m-%d")
                                checkout = datetime.datetime.strftime(dates2[i][2], "%Y-%m-%d")
                                check_in = datetime.datetime.strptime(checkin, '%Y-%m-%d')
                                check_out = datetime.datetime.strptime(checkout, '%Y-%m-%d')
                                # print((dates2[i][0],) )
                                if check_in<=date_in2<=check_out or date_in2<=check_in<=date_out2:
                                    if (dates2[i][0], ) in roomid2:
                                        roomid2.remove((dates2[i][0],))

                            if len(roomid2)>0:
                                room_id = roomid2[0][0]
                                query = f"insert into reservation (room_id, visitor_id, check_in, check_out) values ({room_id}, {visitor_id[0][0]}, '{date_in}', '{date_out}')"
                                cursor.execute(query)
                                db.commit()
                            else:
                                sad_window=tk.Tk()
                                sad_window.title("sad info")
                                sad_window.geometry("200x100+750+650")
                                sad_lab=tk.Label(sad_window, text=f"Sorry, all {rooms} rooms are booked\nYou can try to search other rooms").pack()
                                sad_window.mainloop()
                            print(date_in, date_out, room_type)
                        if (1, ) in bl:######################################
                            
                            warning=tk.Tk()
                            warning.configure(bg="white")
                            warning.title("warning")
                            warning.geometry("300x100+750+300")
                            warning_lab=tk.Label(warning, text='You are in black list,\nso from your card would be deducted the full amount', bg="white")
                            warning_lab.place(x=10, y = 10)
                            ok = tk.Button(warning, text="ok", bg="white", command= opening).place(x=100, y=40) 
                            not_ok = tk.Button(warning, text="not ok", bg="white", command=clear).place(x=150, y=40)
                            warning_lab.place(x=0, y=0)
                        else:
                            opening()
            name=name_entry.get()
            password=password_entry.get()
            pattern_phone="^[0-9]{11}$"
        
            if name!="" and password!="":
                names = "select user_name from visitors"
                cursor.execute(names)
                n = cursor.fetchall()
                passw = f"select passw from visitors where user_name = '{name}'"
                cursor.execute(passw)
                p = cursor.fetchall()
                if (name,) in n:
                    if (password,) in p:
                        sigh_in.destroy()
                        #new window for reservation
                        reservation=tk.Tk()
                        reservation.configure(bg="white")
                        reservation.title("reservation")
                        reservation.geometry("600x250+500+200")
                        var1= tk.IntVar(reservation)

                        var2=tk.IntVar(reservation)

                        #date fields
                        date1_year=tk.Entry(reservation)
                        date1_year.place(x=10, y=60, width=50, height=30)
                        date1_month=tk.Entry(reservation)
                        date1_month.place(x=70, y=60, width=30, height=30)
                        date1_day=tk.Entry(reservation)
                        date1_day.place(x=110, y=60, width=30, height=30)
                        date2_year=tk.Entry(reservation)
                        date2_year.place(x=10, y=120, width=50, height=30)
                        date2_month=tk.Entry(reservation)
                        date2_month.place(x=70, y=120, width=30, height=30)
                        date2_day=tk.Entry(reservation)
                        date2_day.place(x=110, y=120, width=30, height=30)
                        #labels for dates
                        date1_lab=tk.Label(reservation, text="Choose the arrival date (yy/mm/dd):", bg="white")
                        date1_lab.place(x=10, y=32)
                        date2_lab=tk.Label(reservation, text="Choose the arrival date (yy/mm/dd):", bg="white")
                        date2_lab.place(x=10, y=92)
                        #label for room type
                        room_type=tk.Label(reservation, text="room type:", bg="white")
                        room_type.place(x=290, y=45)
                        #label for payment
                        payment=tk.Label(reservation, text="payment method:", bg="white")
                        payment.place(x=430, y=60)
                        #tick buttons
                        econom_tick=tk.Radiobutton(reservation, text="econom",bg="white", variable=var1, value=0)
                        luxe_tick=tk.Radiobutton(reservation, text="luxe",bg="white",variable=var1, value=1)
                        president_tick=tk.Radiobutton(reservation, text="president",bg="white",variable=var1, value=2)
                        econom_tick.place(x=290, y=65)
                        luxe_tick.place(x=290, y=95)
                        president_tick.place(x=290, y=125)
                        #payment tick buttons
                        card=tk.Radiobutton(reservation, text="by card", bg="white", variable=var2, value=0)
                        cash=tk.Radiobutton(reservation, text="by cash", bg="white", variable=var2, value=1)
                        card.place(x=430, y=80)
                        cash.place(x=430, y=100)

                        reserve=tk.Button(reservation, text="reserve",bg="white", font=("AC Boucle", 20), command=result).place(x=240, y=180)
                    else:
                        error_window=tk.Tk()
                        error_window.title("error")
                        error_window.geometry("200x100+750+650")
                        error_lab=tk.Label(error_window, text="password is not correct(").pack()
                else:
                    error_window=tk.Tk()
                    error_window.title("error")
                    error_window.geometry("200x100+750+650")
                    error_lab=tk.Label(error_window, text="user is not found(").pack()
                
                
            else:
                error_lab=tk.Label(sigh_in, text="*fields can`t be empty", bg="white")
                error_lab.place(x=120, y=190)
        choose.destroy()
        sigh_in=tk.Tk()
        sigh_in.title("sigh in")
        sigh_in.configure(bg="white")
        sigh_in.geometry("500x300+500+200")
        #welcome label
        welcome=tk.Label(sigh_in, text="Welcome to our Hotel! If you already have an account, please, sigh in:", font=("Pobeda", 20), bg="white")
        welcome.place(x=0, y=40)
        password_entry=tk.Entry(sigh_in)
        password_entry.config(show="*")
        name_entry=tk.Entry(sigh_in)
        name_entry.place(x=120, y=100, width=350, height=40)
        password_entry.place(x=120, y=150, width=350, height=40)
        name_lab=tk.Label(sigh_in, text="Name: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=110)
        password_lab=tk.Label(sigh_in, text="Password: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=160)
        sigh_in_button=tk.Button(sigh_in,text="sigh_in", bg="white", font=("AC Boucle", 30),command=check_entry).place(x=120, y=210)
    choose=tk.Tk()
    choose.configure(bg="white")
    choose.title("choose")
    choose.geometry("600x200+500+200")
    register_text=tk.Label(choose, text="If you haven`t account yet:", bg="white", font=("AC Boucle", 15)).place(x=310, y=50)
    sighin_text=tk.Label(choose, text="If you already have an account:",bg="white",  font=("AC Boucle", 15)).place(x=10, y=50)
    register_button=tk.Button(choose, text="registration", bg="white", font=("AC Boucle", 20), command=register).place(x=330, y=100)
    sighin_button=tk.Button(choose, text="sign in", bg="white",font=("AC Boucle", 20),  command= sighin ).place(x=80, y=100)
    
    
def click_sighin_button(): #sigh in button
    def check_entry():
        name=name_entry.get()
        password=password_entry.get()
        if name!="" and password!="":
            names = "select user_name from visitors"
            cursor.execute(names)
            n = cursor.fetchall()
            passw = f"select passw from visitors where user_name = '{name}'"
            cursor.execute(passw)
            p = cursor.fetchall()
            if (name,) in n:
                if (password,) in p:
                    def make_txt():
                        txt_window.destroy()
                        welcome.destroy()
                        visitorid = f"select id from visitors where user_name ='{name}'"
                        cursor.execute(visitorid)
                        vid = cursor.fetchall()


                        phone = f"select phone_number from visitors where id = {vid[0][0]}"
                        cursor.execute(phone)
                        number = cursor.fetchall()
                        phone_number = number[0][0]

                        data_about_reservation = f"select room_id, check_in, check_out from reservation where visitor_id = {vid[0][0]}"
                        cursor.execute(data_about_reservation)
                        data = cursor.fetchall()

                        print(data)

                        txt = open("reservation data.txt", "w")
                        txt.write(f"Hello, dear {name}!\nThere is info about your reservation in our hotel\nYou have {len(data)} reservation\n")
                        for i in range(len(data)):
                            txt.write(f"\nRoom №{data[i][0]}\nCheck in date: {data[i][1]} 10am\nCheck out date: {data[i][2]} 12pm\n")
                        txt.write(f"\nWe were glad to serve you, you are welcome any time!")
                        good_window=tk.Tk()
                        good_window.title("good")
                        good_window.geometry("200x100+750+650")
                        good_lab=tk.Label(good_window, text="Your txt file was downloaded \nto the folder \nwhere you saved our hotel ;-)").pack()
                        
                    txt_window=tk.Tk()
                    txt_window.title("getting your data")
                    txt_window.configure(bg="white")
                    txt_window.geometry("200x100+750+650")
                    txt_button=tk.Button(txt_window, text="get my txt!", bg="white", command = make_txt).place(x=0, y=0, width=200, height=100)
                    
                else:
                    error_window=tk.Tk()
                    error_window.title("error")
                    error_window.geometry("200x100+750+650")
                    error_lab=tk.Label(error_window, text="password is not correct(").pack()
            else:
                error_window=tk.Tk()
                error_window.title("error")
                error_window.geometry("200x100+750+650")
                error_lab=tk.Label(error_window, text="user is not found(").pack()
                print(name, password)
        else:
            error_lab=tk.Label(sigh_in, text="*fields can`t be empty", bg="white")
            error_lab.place(x=120, y=190)
        

        
    sigh_in=tk.Tk()
    sigh_in.title("sigh in")
    sigh_in.configure(bg="white")
    sigh_in.geometry("700x320+500+200")
    #welcome label
    welcome=tk.Label(sigh_in, text="Welcome to our Hotel! If you already have an account, please, sigh in:", font=("Pobeda", 20), bg="white")
    welcome.place(x=0, y=40)
    password_entry=tk.Entry(sigh_in)
    password_entry.config(show="*")
    name_entry=tk.Entry(sigh_in)
    name_entry.place(x=120, y=100, width=350, height=40)
    password_entry.place(x=120, y=150, width=350, height=40)
    name_lab=tk.Label(sigh_in, text="Name: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=110)
    password_lab=tk.Label(sigh_in, text="Password: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=160)
    sigh_in_button=tk.Button(sigh_in,text="sigh_in", bg="white", font=("AC Boucle", 30),command=check_entry).place(x=120, y=230)
    


window = tk.Tk()
window.geometry("1500x1300+0+200")
window.configure(bg="white")
window.title("Adel&Sabina hotel")

#label for image
img1=tk.PhotoImage(file="roomss.png")
img_label=tk.Label(window, image=img1)
img_label.place(relx=0, rely=1.0)
img_label.image_ref= img1


#labels for rooms
econom_label=tk.Label(window, text="Econom room", bg="white", font=("Pobeda", 40)).place(x=90, y=530)
luxe_label=tk.Label(window, text="Luxe room", bg="white", font=("Pobeda", 40)).place(x=1100, y=530)
president_label=tk.Label(window, text="President room", bg="white", font=("Pobeda", 40)).place(x=600, y=530)
econom_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=90, y=580)
luxe_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=1100, y=580)
president_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=600, y=580)
econom_size_dig_label=tk.Label(window, text="21m2     2             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=90, y=615)
luxe_size_dig_label=tk.Label(window, text="32m2     2             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=1100, y=615)
president_size_dig_label=tk.Label(window, text="47m2     4             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=600, y=615)
econom_price_label=tk.Label(window, text="30.000KZT/day", bg="white", font=("Pobeda", 25)).place(x=90, y=640)
president_price_label=tk.Label(window, text="60.000KZT/day", bg="white", font=("Pobeda", 25)).place(x=600, y=640)
luxe_price_label=tk.Label(window, text="45.000KZT/day", bg="white", font=("Pobeda", 25)).place(x=1100, y=640)
#buttons
reservation_button=tk.Button(window, text="reservation", bg="white",font=("Pobeda", 60), command=click_reservation_button).place(x=140, y=690 , width=350, height=100)
getinfo_button=tk.Button(window, bg="white",text="GET INFO",  font=("Pobeda", 60) ,command=click_sighin_button).place(x=1030, y=690 , width=300, height=100)
check_out_button=tk.Button(window, text="cancel",bg="white" ,font=("Pobeda", 60), command=click_check_out_button).place(x=600, y=690 , width=300, height=100)

img_label.pack()
window.mainloop()