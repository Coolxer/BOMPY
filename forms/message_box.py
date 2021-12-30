import tkinter as tk
from tkinter import ttk

from forms.modal import Modal
from components.button import Button


class MessageBox(Modal):
    def __init__(
        self, window, title, size, message, confirm_callback, confirm_args=None
    ):
        super().__init__(
            window=window,
            data={},
            item_name={},
            title=title,
            size=size,
            message=message,
            confirm_text="OK",
            hide_buttons=True,
        )

        self.confirm_callback = confirm_callback
        self.confirm_args = confirm_args

        super().get_buttons()[0].grid(
            row=1,
            column=1,
            padx=10,
            pady=10,
        )

    def confirm(self):
        self.confirm_callback(self.confirm_args)
