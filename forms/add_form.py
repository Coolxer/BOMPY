import tkinter as tk
from tkinter import ttk

from forms.object_form import ObjectForm


class AddForm(ObjectForm):
    def __init__(self, window, data, item_name):
        super().__init__(
            window=window,
            data=data,
            item_name=item_name,
            title="Dodawanie obiektu",
            size=(400, 400),
            message="Dodawanie obiektu",
            confirm_text="Dodaj",
        )

    def confirm(self):
        print("confirm add")

    def cancel(self):
        print("cancel add")
