import tkinter as tk
from tkinter import ttk

from forms.modal import Modal


class RemoveDialog(Modal):
    def __init__(self, window, data, item):
        super().__init__(
            window=window,
            data=data,
            item=item,
            title="Usuwanie obiektu",
            size=(500, 100),
            message="Czy jesteś pewien, że chcesz usunąć ten obiekt?",
            confirm_text="Usuń",
        )

    def confirm(self):
        print("confirm remove")

    def cancel(self):
        print("cancel remove")
