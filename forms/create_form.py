import tkinter as tk

from config import PAGES, PALETTE, FONTS
import core.store as store

from components.text import SectionHeader, NormalText
from components.button import Button
from components.input import Input

from forms.modal import Modal
from forms.message_box import MessageBox

# klasa formularza tworzenia nowego zestawienia
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

    # metoda sprawdza poprawność danych i ewentualnie zapisuje dane w pliku
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
            store.instance.set_project_name(name_output)
            store.instance.get_file_manager().open_to_write()

    # metoda tworzy widżety niezbędne dla tego okna
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
