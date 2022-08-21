from tkinter import *
import math


def calc():
    user_input = float(mi_input.get())
    ans_lbl.config(text=f"{round(user_input*1.6, 2)}")

window = Tk()
window.minsize(height=100, width=300)
window.config(padx=30 ,pady=15)

mi_input = Entry()
mi_input.insert(0, string="0")
mi_input.grid(column=1, row=0)

mi_lbl = Label()
mi_lbl.config(text="Miles")
mi_lbl.grid(column=2,row=0)

km_lbl = Label()
km_lbl.config(text="Kilometers")
km_lbl.grid(column=2, row=1)

intro_lbl = Label()
intro_lbl.config(text="is equal to")
intro_lbl.grid(column=0, row=1)

ans_lbl = Label()
ans_lbl.config(text="0")
ans_lbl.grid(column=1, row=1)

calc_btn = Button(text="Calculate", command=calc)
calc_btn.grid(column=1,row=2)



window.mainloop()