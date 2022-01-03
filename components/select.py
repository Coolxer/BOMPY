from tkinter import OptionMenu, StringVar

from config import FONTS, PALETTE

# klasa wyboru opcji z listy
class Select(OptionMenu):
    def __init__(self, window, values):
        self.value = StringVar()
        self.value.set(values[0])
        super().__init__(window, self.value, *values)

        self["width"] = 15
        self["foreground"] = PALETTE["PRIMARY"]
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = FONTS["NORMAL_TEXT"]

        self["activebackground"] = PALETTE["PRIMARY"]
        self["activeforeground"] = PALETTE["BACKGROUND"]
        self["borderwidth"] = 5
        self["relief"] = "solid"

    # metoda zwraca wybraną opcję
    def get_value(self):
        return self.value.get()

    # metoda ustawia opcję
    def set_value(self, value):
        self.value.set(value)
