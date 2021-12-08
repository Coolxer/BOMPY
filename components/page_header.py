import tkinter as tk

from config import PALETTE, FONTS


class PageHeader(tk.Label):
    def __init__(self, window, text):
        super().__init__(window)

        self["text"] = text
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["PAGE_HEADER"]