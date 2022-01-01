import tkinter as tk

from functools import partial

from config import PALETTE, FONTS


class Input(tk.Entry):
    def __init__(
        self,
        window,
        input_name,
        content_type,
        min_length=None,
        max_length=None,
        placeholder=None,
    ):
        super().__init__(window, justify="center")

        self["width"] = 20
        # self["height"] = 3
        self["text"] = placeholder
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["NORMAL_TEXT"]

        self.input_name = input_name
        self.content_type = content_type
        self.min_length = min_length
        self.max_length = max_length

    def validate(self):
        value = self.get_value()

        if self.min_length is not None and len(value) < self.min_length:
            return f"{self.input_name} musi mieć co najmniej {self.min_length} znaków długości"
        elif self.max_length is not None and len(value) > self.max_length:
            return f"{self.input_name} może mieć maksymalnie {self.max_length} znaków długości"
        else:
            if self.content_type == "string":
                return ""
            elif self.content_type == "integer":
                try:
                    int(value)
                    return ""
                except ValueError:
                    return f"{self.input_name} musi być liczbą"
            elif self.content_type == "float":
                try:
                    float(value.replace(",", "."))
                    return ""
                except ValueError:
                    return f"{self.input_name} musi być liczbą"
            else:
                return ""

    def get_value(self):
        return self.get()
