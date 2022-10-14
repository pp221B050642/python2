from tkinter import *
# root = Tk()
# widget = Label(root, text = 'Hello World!')
# widget.pack(side = BOTTOM)
# # widget.grid(column = 2, row = 1)
# root.mainloop()

top = Tk()

# def button_func():
#     print("hello")

def button_func(event):
    new_window = Tk()
    Label(new_window, text = "welcome").pack()
    new_window.mainloop()

B = Button(top, text = "Press")
B.bind('<Button-3>', button_func)#right
B.pack()
top.mainloop()
