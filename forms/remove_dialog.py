import tkinter as tk
from tkinter import ttk

from forms.modal import Modal


class RemoveDialog(Modal):
    def __init__(self, window, data, item, callback):
        super().__init__(
            window=window,
            data=data,
            item=item,
            title="Usuwanie obiektu",
            size=(500, 100),
            message="Czy chcesz usunąć ten obiekt?",
            confirm_text="Usuń",
        )

        self.data = data
        self.name = item
        self.callback = callback

    def confirm(self):
        self.recursive(self.data)
        self.callback()
        # print("confirm remove")

    def recursive(self, item, index=0):
        if item["name"] == self.name:
            return index

        index = 0
        for el in item["sub_parts"]:
            result = self.recursive(el, index)
            if result >= 0:
                item["sub_parts"].pop(result)
                break

            index += 1

        return -1

    def cancel(self):
        print("cancel remove")
