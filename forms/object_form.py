import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.section_header import SectionHeader
from components.button import Button
from components.input import Input
from components.select import Select

from forms.modal import Modal
from core.units import UNITS


class ObjectForm(Modal):
    def __init__(self, window, data, item, title, size, message, confirm_text):
        super().__init__(
            window=window,
            data=data,
            item=item,
            title=title,
            size=size,
            message=message,
            confirm_text=confirm_text,
            hide_buttons=True,
        )

        self.create_widgets()

    def confirm(self):
        print("confirm")

    def cancel(self):
        print("cancel")

    def create_widgets(self):
        self.name_input = Input(
            window=super().get_frame(),
            content_type="string",
            min_length=3,
            max_length=10,
        )
        self.identifier_input = Input(
            window=super().get_frame(),
            content_type="int",
            min_length=6,
            max_length=6,
        )
        self.unit_input = Select(window=super().get_frame(), values=UNITS)
        self.unit_cost_input = Input(
            window=super().get_frame(),
            content_type="float",
            min_length=1,
            max_length=9,
        )

        self.name_input.grid(row=0, column=0)
        self.identifier_input.grid(row=1, column=0)
        self.unit_input.grid(row=2, column=0)
        self.unit_cost_input.grid(row=3, column=0)

    def validate(self):
        if not self.name_input.validate():
            print("invalid name")
