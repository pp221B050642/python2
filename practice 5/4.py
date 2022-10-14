from tkinter import *
import mysql.connector as mysql
top = Tk()

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Fairy.tale01",
    database = "test")

cursor = db.cursor()



name = Label(top, text = "User name")
name.grid(column=0, row=0)
password = Label(top, text = "Password")
password.grid(column = 0, row=1)

E1 = Entry(top)
E1.grid(column = 1,row=0 )
E2 = Entry(top)
E2.grid(column = 1, row = 1)

def helloCallBack(event):
    user_name = E1.get()
    passw = E2.get()
    passwords = "SELECT password  FROM tkinter_users where user_name=%s"
    cursor.execute(passwords, (user_name,))
    p = cursor.fetchall()
    names = "SELECT user_name  FROM tkinter_users"
    cursor.execute(names)
    n = cursor.fetchall()
    new_window = Tk()
    if (user_name,) in n:
        if (passw,) in p:
            Label(new_window, text = "welcome").pack()
            new_window.mainloop()
        else:
            Label(new_window, text = "Password is not correct").pack()
            new_window.mainloop()
    else:
        Label(new_window, text = "user is not found").pack()
        new_window.mainloop()
    # if user_name in names:
    #     if passw == :
    #         Label(new_window, text = "welcome").pack()
    #         new_window.mainloop()
    #     else:
    #         Label(new_window, text = "Password is not correct").pack()
    #         new_window.mainloop()
    # else:
    #     Label(new_window, text = "user is not found").pack()
    #     new_window.mainloop()


B = Button(top, text = "Press")
B.bind('<Button-1>', helloCallBack)#left
B.grid()
top.mainloop()