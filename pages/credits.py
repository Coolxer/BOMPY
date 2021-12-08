import tkinter as tk

from config import PAGES


class Credits(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)
        tk.Button(
            self,
            text="Go to menu",
            command=lambda: parent.switch_scene(PAGES["MENU"]),
            font=("arial", 100),
        ).pack()

        print("herte")
