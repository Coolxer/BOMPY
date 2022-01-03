from tkinter import Button as Btn
from functools import partial

from config import PALETTE, FONTS

# klasa przycisku
class Button(Btn):
    def __init__(self, window, text, type, command, arg=None):
        super().__init__(window)

        command_with_arg = partial(command, arg)

        if arg is not None:
            cmd = command_with_arg
        else:
            cmd = command

        self["width"] = 20
        self["height"] = 3
        self["text"] = text
        self["foreground"] = PALETTE["BACKGROUND"]
        self["background"] = PALETTE[type]
        self["font"] = FONTS["COMPONENT"]
        self["command"] = cmd

    # metoda ustawia stan przycisku
    def set_state(self, state):
        self["state"] = state
