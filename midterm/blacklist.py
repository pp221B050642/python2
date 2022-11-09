import tkinter as tk

# warning=tk.Tk()
# warning.configure(bg="white")
# warning.title("warning")
# warning.geometry("300x100+750+300")
# warning_lab=tk.Label(warning, text="""You are in black list, 
# so from your card would be deducted the full amount""", bg="white")
# ok = tk.Button(warning, text="ok", bg="white").place(x=100, y=40) 
# not_ok = tk.Button(warning, text="not ok", bg="white").place(x=150, y=40)
# warning_lab.place(x=0, y=0)
# warning.mainloop()

sad_window=tk.Tk()
sad_window.title("sad info")
sad_window.geometry("200x100+750+650")
sad_lab=tk.Label(sad_window, text=f"Sorry, all  rooms are booked\nYou can try to search other rooms").pack()
sad_window.mainloop()