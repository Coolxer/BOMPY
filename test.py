# importing all files  from tkinter
from tkinter import *
from tkinter import ttk

import tkinter as tk

from tkinter.filedialog import asksaveasfile

import json

root = Tk()
root.geometry("200x150")

data = {}


def save():
    data = {"application": "bumpy"}

    file_path = tk.filedialog.asksaveasfilename(
        title="Wybierz lokalizację pliku zestawienia",
        filetypes=(("json", "*.json"),),
    )


btn = ttk.Button(root, text="Save", command=lambda: save())
btn.pack(side=TOP, pady=20)


mainloop()
