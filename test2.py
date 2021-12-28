from tkinter import *

root = Tk()
root.title("title")

root.geometry("400x400")

units = ["one", "two", "three", "four"]

var = StringVar()
var.set(units[0])


dropdown = OptionMenu(root, var, *units)
dropdown.pack()

print(var.get())

root.mainloop()
