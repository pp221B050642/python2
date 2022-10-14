from tkinter import *
top = Tk()

l1 = Label(top, text = "User name")
l1.pack(side = LEFT)

E1 = Entry(top)
E1.pack(side = RIGHT)

def helloCallBack(event):
    user_name = E1.get()
    print(user_name)

B = Button(top, text = "Press")
B.bind('<Button-1>', helloCallBack)#left
B.pack(side = BOTTOM)
top.mainloop()