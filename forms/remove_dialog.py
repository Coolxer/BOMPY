import tkinter as tk
from tkinter import ttk

from forms.modal import Modal


class RemoveDialog(Modal):
    def __init__(self, window, data, item_name, remove_callback):
        super().__init__(
            window=window,
            data=data,
            item_name=item_name,
            title="Usuwanie obiektu",
            size=(500, 100),
            message="Czy chcesz usunąć ten obiekt?",
            confirm_text="Usuń",
        )

        self.remove_callback = remove_callback

    def confirm(self):
        self.recursive(super().get_data())
        self.remove_callback()

    def recursive(self, item, index=0):
        if item["name"] == super().get_item_name():
            return index

        index = 0
        for el in item["sub_parts"]:
            result = self.recursive(el, index)
            if result >= 0:
                item["sub_parts"].pop(result)
                break

            index += 1

        return -1
