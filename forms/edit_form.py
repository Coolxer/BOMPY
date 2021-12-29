import tkinter as tk
from tkinter import ttk

from forms.object_form import ObjectForm


class EditForm(ObjectForm):
    def __init__(self, window, data, item):
        super().__init__(
            window=window,
            data=data,
            item=item,
            title="Edytowanie obiektu",
            size=(400, 400),
            message="Edytowanie obiektu",
            confirm_text="Zapisz",
        )

    def confirm(self):
        print("confirm edit")

    def cancel(self):
        print("cancel edit")
