import tkinter as tk
from tkinter import ttk

from forms.object_form import ObjectForm


class AddForm(ObjectForm):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Dodawanie obiektu",
            size=(600, 400),
            message="Dodawanie obiektu",
            confirm_text="Dodaj",
        )

    def confirm(self):
        print("confirm add")

    def cancel(self):
        print("cancel add")
