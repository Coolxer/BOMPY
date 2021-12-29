import tkinter as tk


class Select(tk.OptionMenu):
    value = None

    def __init__(self, window, values):
        self.value = tk.StringVar()
        self.value.set(values[0])

        super().__init__(window, self.value, values)

    def get_value(self):
        return self.value.get()
