import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.normal_text import NormalText
from components.button import Button
from components.input import Input
from components.select import Select

from forms.modal import Modal
from core.units import UNITS


class ObjectForm(Modal):
    def __init__(
        self, window, data, item_name, title, size, message, confirm_text
    ):
        super().__init__(
            window=window,
            data=data,
            item_name=item_name,
            title=title,
            size=size,
            message=message,
            confirm_text=confirm_text,
            hide_buttons=True,
            rows=[0, 1, 2, 3, 4, 5],
            columns=[0, 1, 2, 3],
        )

        self.create_widgets()

    def confirm(self):
        print("confirm")

    def cancel(self):
        print("cancel")

    def create_widgets(self):
        self.identifier_label = NormalText(
            window=super().get_frame(), text="Identyfikator"
        )
        self.identifier_input = Input(
            window=super().get_frame(),
            content_type="int",
            min_length=6,
            max_length=6,
        )

        self.name_label = NormalText(window=super().get_frame(), text="Nazwa")
        self.name_input = Input(
            window=super().get_frame(),
            content_type="string",
            min_length=3,
            max_length=10,
        )

        self.unit_label = NormalText(
            window=super().get_frame(), text="Jednostka"
        )
        self.unit_input = Select(window=super().get_frame(), values=UNITS)

        self.unit_cost_label = NormalText(
            window=super().get_frame(), text="Cena jedn."
        )
        self.unit_cost_input = Input(
            window=super().get_frame(),
            content_type="float",
            min_length=1,
            max_length=9,
        )

        self.identifier_label.grid(row=1, column=1)
        self.name_label.grid(row=2, column=1)
        self.unit_label.grid(row=3, column=1)
        self.unit_cost_label.grid(row=4, column=1)

        self.identifier_input.grid(row=1, column=2)
        self.name_input.grid(row=2, column=2)
        self.unit_input.grid(row=3, column=2)
        self.unit_cost_input.grid(row=4, column=2)

        super().show_buttons((5, 0), (5, 3))

    def validate(self):
        if not self.name_input.validate():
            print("invalid name")
