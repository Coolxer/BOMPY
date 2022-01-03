from tkinter import Entry
from functools import partial
from config import PALETTE, FONTS

# klasa interaktywnego pola tekstowego
class Input(Entry):
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
        self["text"] = placeholder
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["NORMAL_TEXT"]

        self.input_name = input_name
        self.content_type = content_type
        self.min_length = min_length
        self.max_length = max_length

    # metoda mapuje długość na odpowiednią formę słowa 'znak'
    def characters_string(self, length):
        if length <= 1:
            return "znak"
        elif length <= 4:
            return "znaki"
        else:
            return "znaków"

    # metoda sprawdza poprawność danych wpisanych do pola edycji
    def validate(self):
        value = self.get_value()
        length = len(value)

        if self.min_length is not None and length < self.min_length:
            return f"{self.input_name} musi mieć co najmniej {self.min_length} {self.characters_string(self.min_length)} długości"
        elif self.max_length is not None and length > self.max_length:
            return f"{self.input_name} może mieć maksymalnie {self.max_length} {self.characters_string(self.max_length)} długości"
        else:
            if self.content_type == "string":
                return ""
            elif self.content_type == "int":
                try:
                    int(value)
                except ValueError:
                    return f"{self.input_name} musi być liczbą"
            elif self.content_type == "float":
                try:
                    float(value.replace(",", "."))
                except ValueError:
                    return f"{self.input_name} musi być liczbą"
            else:
                return ""

        return ""

    # metoda zwraca wartość pola edycji
    def get_value(self):
        return self.get()
