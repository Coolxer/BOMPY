import tkinter as tk
from tkinter import ttk

from forms.object_form import ObjectForm


class EditForm(ObjectForm):
    def __init__(self, window, data, item_name):
        super().__init__(
            window=window,
            data=data,
            item_name=item_name,
            title="Edytowanie obiektu",
            size=(600, 400),
            message="Edytowanie obiektu",
            confirm_text="Zapisz",
        )
