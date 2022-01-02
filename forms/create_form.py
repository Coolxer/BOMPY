import tkinter as tk

from config import PAGES, PALETTE, FONTS
import core.store as store

from components.normal_text import NormalText
from components.section_header import SectionHeader
from components.button import Button
from components.input import Input

from forms.modal import Modal
from forms.message_box import MessageBox


class CreateForm(Modal):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Tworzenie BOM",
            size=(700, 200),
            message="Tworzenie nowego zestawienia BOM",
            confirm_text="Utwórz",
            confirm_auto_destroy=False,
            hide_buttons=True,
            rows=[0, 1, 2],
            columns=[0, 1, 2, 3],
        )
        self.create_widgets()

    def confirm(self):
        name_output = self.name_input.validate()

        if len(name_output):
            msg_box = MessageBox(
                window=self,
                title="Nieprawidłowe dane",
                size=(700, 150),
                message=name_output,
            )
        else:
            super().get_frame().destroy()
            self.open_file_dialog()
            store.instance.call_switch_scene(PAGES["WORKPAGE"])

    def create_widgets(self):
        self.name_label = NormalText(window=super().get_frame(), text="Nazwa")
        self.name_input = Input(
            window=super().get_frame(),
            input_name="Nazwa",
            content_type="string",
            min_length=3,
            max_length=10,
        )

        self.name_label.grid(row=1, column=1)
        self.name_input.grid(row=1, column=2)

        super().show_buttons((2, 0), (2, 3))

    def open_file_dialog(self):
        file = tk.filedialog.asksaveasfilename()(
            title="Wybierz lokalizację pliku zestawienia",
            filetypes=(("Bompy file", "*.json"),),
            defaultextension="*.json",
        )

        file_manager = FileManager(file)

        data = {}
