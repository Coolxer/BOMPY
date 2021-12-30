import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.section_header import SectionHeader
from components.button import Button
from components.input import Input

from forms.modal import Modal


class CreateForm(Modal):
    def __init__(self, window):
        super().__init__(
            window=window,
            data={},
            item_name=None,
            title="Tworzenie BOM",
            size=(600, 200),
            message="Tworzenie nowego zestawienia BOM",
            confirm_text="Utwórz",
            hide_buttons=True,
            rows=[0, 1, 2],
            columns=[0, 1],
        )

        self.create_widgets()

    def confirm(self):
        print("confirm")

    def create_widgets(self):
        self.name_input = Input(
            window=super().get_frame(),
            content_type="string",
            min_length=3,
            max_length=10,
        )

        self.name_input.grid(row=1, column=1)
        super().show_buttons((2, 0), (2, 2))
