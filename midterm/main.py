import mysql.connector as mysql
import tkinter as tk


def click_check_out_button():  #checking out function
    def check_entry():
        global checkout_name, checkout_password
        checkout_name=name_entry.get()
        checkout_password=password_entry.get()
    checkout=tk.Tk()
    checkout.title("checking out")
    checkout.configure(bg="white")
    checkout.geometry("500x500+500+200")
    password_entry=tk.Entry(checkout)
    password_entry.place(x=50, y=150, width=350, height=40)
    password_entry.config(show="*")
    name_entry=tk.Entry(checkout)
    name_entry.place(x=50, y=100, width=350, height=40)
    sigh_in_button=tk.Button(checkout,text="check out", bg="white", font=("AC Boucle", 30), command=check_entry).place(x=50, y=210)



def click_reservation_button(): #reservation button
    def check_entry():
        global register_name, register_number, register_password
        register_name=name_entry.get()
        register_password=password_entry.get()
        register_number=number_entry.get()
    reservation=tk.Tk()
    reservation.configure(bg="white")
    reservation.title("reservation")
    reservation.geometry("500x500+500+200")
    name_entry=tk.Entry(reservation, text="name")
    name_entry.place(x=120, y=100, width=350, height=40)
    number_entry=tk.Entry(reservation)
    number_entry.place(x=120, y=150, width=350, height=40)
    make_res=tk.Label(reservation, text="Please, register first", bg="white", font=("AC Boucle", 20)).place(x=30, y=60)
    name_lab=tk.Label(reservation, text="Name: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=110)
    number_lab=tk.Label(reservation, text="Phone: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=160)
    password_lab=tk.Label(reservation, text="Password: ", bg="white", font=("AC Boucle", 20)).place(x=10, y=210)
    password_entry=tk.Entry(reservation)
    password_entry.config(show="*")
    password_entry.place(x=120, y=200, width=350, height=40)
    register_button=tk.Button(reservation,text="registration",  bg="white", font=("AC Boucle", 30), command=check_entry).place(x=120, y=260)


def click_sighin_button(): #sigh in button
    def check_entry():
        global sighin_name, sighin_password
        sighin_name=name_entry.get()
        sighin_password=password_entry.get()
    sigh_in=tk.Tk()
    sigh_in.title("sigh in")
    sigh_in.configure(bg="white")
    sigh_in.geometry("500x500+500+200")
    password_entry=tk.Entry(sigh_in)
    password_entry.config(show="*")
    password_entry.place(x=50, y=150, width=350, height=40)
    name_entry=tk.Entry(sigh_in)
    name_entry.place(x=50, y=100, width=350, height=40)
    sigh_in_button=tk.Button(sigh_in,text="sigh_in", bg="white", font=("AC Boucle", 30),command=check_entry).place(x=50, y=210)


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
econom_label=tk.Label(window, text="Econom room", bg="white", font=("Pobeda", 40)).place(x=90, y=540)
luxe_label=tk.Label(window, text="Luxe room", bg="white", font=("Pobeda", 40)).place(x=1100, y=540)
president_label=tk.Label(window, text="President room", bg="white", font=("Pobeda", 40)).place(x=600, y=540)
econom_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=90, y=590)
luxe_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=1100, y=590)
president_size_label=tk.Label(window, text="size     pers    bathroom", bg="white", font=("Pobeda", 20)).place(x=600, y=590)
econom_size_dig_label=tk.Label(window, text="21m2     2             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=90, y=615)
luxe_size_dig_label=tk.Label(window, text="32m2     2             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=1100, y=615)
president_size_dig_label=tk.Label(window, text="47m2     4             Shower or Bathtub", bg="white", font=("AC Boucle", 15)).place(x=600, y=615)

#buttons
reservation_button=tk.Button(window, text="reservation", bg="white",font=("Bebas Neue", 60), command=click_reservation_button).place(x=170, y=690 , width=300, height=100)
sigh_in_button=tk.Button(window, bg="white",text="sigh in",  font=("Bebas Neue", 60) ,command=click_sighin_button).place(x=1030, y=690 , width=300, height=100)
check_out_button=tk.Button(window, text="check out", font=("Bebas Neue", 60), command=click_check_out_button).place(x=600, y=690 , width=300, height=100)

img_label.pack()
window.mainloop()


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()

def registration():
    """user_name = input()
    user_password = input()
    phone_number = input()"""
    names = 'select user_name from visitors'
    cursor.execute(names)
    n = cursor.fetchall()
    if (register_name,) in n:
        print("user already exits")
    else:
        query = f"insert into visitors (user_name, passw, phine_number) values ('{register_name}', '{register_password}', '{register_number}')"
        cursor.execute(query)
        db.commit()

def sign_in():
    """user_name = input()
    user_password = input()"""
    names = "select user_name from visitors"
    cursor.execute(names)
    n = cursor.fetchall()
    passw = f"select passw from visitors where user_name = '{sighin_name}'"
    cursor.execute(passw)
    p = cursor.fetchall()
    if (sighin_name,) in n:
        if (sighin_password,) in p:
            print("welcome")
        else:
            print("password is not correct")
    else:
        print("user not found")