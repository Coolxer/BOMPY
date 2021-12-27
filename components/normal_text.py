import tkinter as tk

from config import PALETTE, FONTS


class NormalText(tk.Label):
    def __init__(self, window, text):
        super().__init__(window)

        self["text"] = text
        self["foreground"] = PALETTE["WHITE"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["NORMAL_TEXT"]
        self["wraplength"] = 500
        # self["justify"] = "left"
