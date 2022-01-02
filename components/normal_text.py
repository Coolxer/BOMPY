from tkinter import Label

from config import PALETTE, FONTS


class NormalText(Label):
    def __init__(self, window, text):
        super().__init__(window)

        self["text"] = text
        self["foreground"] = PALETTE["WHITE"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["NORMAL_TEXT"]
        self["wraplength"] = 500
