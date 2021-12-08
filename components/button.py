import tkinter as tk

from functools import partial

from config import PALETTE, FONTS


class Button(tk.Button):
    def __init__(self, window, text, type, action, arg=None):
        super().__init__(window)

        action_with_arg = partial(action, arg)

        if arg is not None:
            act = action_with_arg
        else:
            act = action

        self["width"] = 20
        self["height"] = 3
        self["text"] = text
        self["foreground"] = PALETTE["BACKGROUND"]
        self["background"] = PALETTE[type]
        self["font"] = FONTS["COMPONENT"]
        self["command"] = act
