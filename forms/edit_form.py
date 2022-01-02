import tkinter as tk
from tkinter import ttk

from forms.object_form import ObjectForm


class EditForm(ObjectForm):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Edytowanie obiektu",
            size=(600, 400),
            message="Edytowanie obiektu",
            confirm_text="Zapisz",
        )
