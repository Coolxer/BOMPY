import tkinter as tk

from functools import partial

from config import PALETTE, FONTS


class Input(tk.Entry):
    def __init__(
        self,
        window,
        content_type,
        min_length,
        max_length,
        placeholder=None,
    ):
        super().__init__(window)

        self["width"] = 20
        # self["height"] = 3
        self["text"] = placeholder
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["COMPONENT"]

        self.min_length = min_length
        self.max_length = max_length
        self.content_type = content_type

        self.value = tk.StringVar()
        self.value.trace("w", self.limit)

    def validate(self):
        if self.content_type == "string":
            pass
        elif self.content_type == "integer":
            try:
                int(self.value)
                print("number")
                return True
            except ValueError:
                print("no number")
                return False
        elif self.content_type == "float":
            try:
                float(self.value)
                print("float")
                return True
            except ValueError:
                print("no float")
                return False
        else:
            return False

    def limit(self):
        self.value = self.get()
        if len(self.value) > self.max_length:
            self.value.set(self.value[: self.max_length])
        elif len(self.value) < self.min_length:
            return False

        return True

    def get_value(self):
        return self.value.get()
