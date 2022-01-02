import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.normal_text import NormalText
from components.button import Button
from components.input import Input
from components.select import Select

from forms.modal import Modal
from core.units import UNITS

from forms.message_box import MessageBox


class ObjectForm(Modal):
    def __init__(self, window, title, size, message, confirm_text):
        super().__init__(
            window=window,
            title=title,
            size=size,
            message=message,
            confirm_text=confirm_text,
            confirm_auto_destroy=False,
            hide_buttons=True,
            rows=[0, 1, 2, 3, 4, 5],
            columns=[0, 1, 2, 3],
        )

        self.create_widgets()

    def confirm(self):
        identifier_output = self.identifier_input.validate()
        name_output = self.name_input.validate()
        unit_cost_output = self.unit_cost_input.validate()

        if len(identifier_output) or len(name_output) or len(unit_cost_output):
            msg = ""
            if len(identifier_output):
                msg = identifier_output
            elif len(name_output):
                msg = name_output
            else:
                msg = unit_cost_output

            msg_box = MessageBox(
                window=self,
                title="Nieprawidłowe dane",
                size=(700, 150),
                message=msg,
            )
        else:
            super().get_frame().destroy()

    def create_widgets(self):
        self.identifier_label = NormalText(
            window=super().get_frame(), text="Identyfikator"
        )
        self.name_label = NormalText(window=super().get_frame(), text="Nazwa")
        self.unit_label = NormalText(
            window=super().get_frame(), text="Jednostka"
        )
        self.unit_cost_label = NormalText(
            window=super().get_frame(), text="Cena jedn."
        )

        self.identifier_label.grid(row=1, column=1)
        self.name_label.grid(row=2, column=1)
        self.unit_label.grid(row=3, column=1)
        self.unit_cost_label.grid(row=4, column=1)

        self.identifier_input = Input(
            window=super().get_frame(),
            input_name="Identyfikator",
            content_type="int",
            min_length=6,
            max_length=6,
        )
        self.name_input = Input(
            window=super().get_frame(),
            input_name="Nazwa",
            content_type="string",
            min_length=3,
            max_length=10,
        )
        self.unit_input = Select(window=super().get_frame(), values=UNITS)
        self.unit_cost_input = Input(
            window=super().get_frame(),
            input_name="Cena jedn.",
            content_type="float",
            min_length=1,
            max_length=9,
        )

        self.identifier_input.grid(row=1, column=2)
        self.name_input.grid(row=2, column=2)
        self.unit_input.grid(row=3, column=2)
        self.unit_cost_input.grid(row=4, column=2)

        super().show_buttons((5, 0), (5, 3))
