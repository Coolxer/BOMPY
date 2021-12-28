import tkinter as tk


class Select(tk.OptionMenu):
    current = StringVar()

    def __init__(self, window, values):
        self.current(values[0])

        super().__init__(window, self.current, values)

    def get_value(self):
        return self.current.get()
