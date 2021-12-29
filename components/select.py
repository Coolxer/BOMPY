import tkinter as tk

from config import FONTS, PALETTE


class Select(tk.OptionMenu):
    value = None

    def __init__(self, window, values):
        self.value = tk.StringVar()
        self.value.set(values[0])

        super().__init__(window, self.value, *values)

        self["width"] = 15
        # self["height"] = 2
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["COMPONENT"]

        self["activebackground"] = PALETTE["PRIMARY"]
        self["activeforeground"] = PALETTE["BACKGROUND"]
        self["borderwidth"] = 5
        self["relief"] = "solid"

    def get_value(self):
        return self.value.get()
