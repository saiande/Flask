from tkinter import *
from tkinter import messagebox

master = Tk()
master.title("CSE 337 Drawing Program")
master.geometry("1000x1000")

frameTop = Frame(master)
frameTop.pack()
canvas = Canvas(frameTop, width=500, height=500)
canvas.pack()

frameBottom = Frame(master)
frameBottom.pack()

Label(frameBottom, text = "Param 1").grid(row=0, column=0)
Label(frameBottom, text = "Param 2").grid(row=1, column=0)
Label(frameBottom, text = "Param 3").grid(row=2, column=0)
Label(frameBottom, text = "Param 4").grid(row=3, column=0)
Label(frameBottom, text = "Width").grid(row=4, column=0)

a = Entry(frameBottom)
a.grid(row=0, column=1)

b = Entry(frameBottom)
b.grid(row=1, column=1)

c = Entry(frameBottom)
c.grid(row=2, column=1)

d = Entry(frameBottom)
d.grid(row=3, column=1)

e = Entry(frameBottom)
e.grid(row=4, column=1)

def create():
	if ((not (a.get().isdigit())) or (not (b.get().isdigit())) or (not (c.get().isdigit())) or (not (d.get().isdigit())) or (not (e.get().isdigit())) or int(a.get()) < 0 or int(b.get()) < 0 or int(c.get()) < 0 or int(d.get()) < 0 or int(e.get()) < 0):
		messagebox.showerror("Warning", "Invalid Size")

	elif(v.get() == 1):
		canvas.create_rectangle(a.get(), b.get(), c.get(), d.get(), width=e.get(), outline=color.get())

	elif(v.get() == 2):
		canvas.create_line(a.get(), b.get(), c.get(), d.get(), width=e.get(), fill=color.get())

	elif(v.get() == 3):
		canvas.create_oval(a.get(), b.get(), c.get(), d.get(), width=e.get(), outline=color.get())

v = IntVar()

Radiobutton(frameBottom, text="Rectangle", variable=v, value=1, command=create).grid(row=5, column=1)
Radiobutton(frameBottom, text="Line", variable=v, value=2, command=create).grid(row=6, column=1)
Radiobutton(frameBottom, text="Oval", variable=v, value=3, command=create).grid(row=7, column=1)

color = StringVar()
Radiobutton(frameBottom, text="Red", variable=color, value="red").grid(row=8, column=1)
Radiobutton(frameBottom, text="Green", variable=color, value="green").grid(row=9, column=1)
Radiobutton(frameBottom, text="Blue", variable=color, value="blue").grid(row=10, column=1)
mainloop()