from tkinter import *
from tkinter.ttk import *
from solving import *

root = Tk()
root.title("K-map")
root.geometry("1200x700")
num_of_var = Style()
num_of_var.configure("W.TButton", font=("Steelfish Rg", 25))
name = Style()
name.configure("TButton", font=("Monoton", 50))
bg = PhotoImage(file='math7.png')
user_inp = StringVar()
def minimize():
    circuit = user_inp.get()
    print(circuit)
    answer = solve_it(circuit)
    print(answer)
    t1 = [i for i in answer[0]]
    t1_t = ''
    for i in t1:
        t1_t+=f"{i}\n"
    t2 = set([i for i in answer[1]])
    t2_t =""
    for i in list(t2):
        t2_t+=f"{i}\n"
    final_answer = list(answer[2])
    final_answer_t = "+".join(final_answer)
    step1 = Label(root, text=f"Step 1:\n{t1_t}", font=("times New Roman", 14)).place(x=250, y=350)
    step2 = Label(root, text=f"Step 1:\n{t2_t}", font=("times New Roman", 14)).place(x=350, y=350)
    answer_l = Label(root, text=f"Answer:\n{final_answer_t}", font=("Times New Roman", 14)).place(x=450, y=350)


background = Label(root, image=bg).place(x=0, y=0)
num_label = Label(root, text="K-Map by Adel", style='TButton').pack(pady=50)

wh = Label(root, text="Write here: ", font=("Times New Roman", 18)).place(x=50, y=250)
user_input = Entry(root, textvariable=user_inp, font=("Times New Roman", 14)).place(x=165, y=250, width=400, height=35)

solve_btn = Button(root, text="Solve Map", style="W.TButton", command=minimize)
solve_btn.place(x=600, y=250)

rules = Label(root, text="0-> x, y, z, w\n1-> ~x, ~y, ~z, ~w", font=("Times New Roman", 16)).place(x=50, y=350)

root.mainloop()
