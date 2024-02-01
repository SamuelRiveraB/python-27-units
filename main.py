from tkinter import *

MILE = 0.621371

window = Tk()
window.title("My First GUI Program")
window.minsize(500, 300)
window.config(padx=100, pady=100)

my_label = Label(text="Unit converter", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)


def calc():
    val = int(inp.get())
    num.config(text=val * MILE)


inp = Entry()
inp.grid(column=1, row=1)

kms = Label(text="Kms")
kms.grid(column=2, row=1)

equal = Label(text="is equal to")
equal.grid(column=0, row=2)

num = Label(text="0")
num.grid(column=1, row=2)

miles = Label(text="Miles")
miles.grid(column=2, row=2)

btn = Button(text="Calculate", command=calc)
btn.grid(column=2, row=3)

def add(*args):
    count = 0
    for a in args:
        count += a
    print(count)


add(6, 7, 7, 85, 54, 3)

window.mainloop()
