import tkinter as tk
from tkinter.ttk import *

root = tk.Tk()

root.geometry("215x200")

time_var = tk.IntVar()


def submit():
    time = time_var.get()
    print("Tempo de foco: " , time)

    time_var.set("")


time_label = tk.Label(
    root, text="Digite o tempo que deseja focar: ", font=("calibre", 10, "bold")
)

time_entry = tk.Entry(root, textvariable=time_var, font=("calibre", 10, "normal"))

img = tk.PhotoImage(file='tomate.png').subsample(45,45)

sub_btn = tk.Button(root, image=img, command=submit)
                    #text="Submit", command=submit)

# ...existing code...

time_label.grid(row=0, column=0, columnspan=2, pady=10)
time_entry.grid(row=1, column=0, columnspan=2, pady=10)
sub_btn.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

# ...existing code...


root.mainloop()


