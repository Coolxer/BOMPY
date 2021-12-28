import tkinter as tk

from functools import partial

from config import PALETTE, FONTS


class Input(tk.Entry):
    def __init__(self, window, text=None):
        super().__init__(window)

        self["width"] = 20
        # self["height"] = 3
        self["text"] = text
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["COMPONENT"]
