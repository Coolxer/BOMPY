import tkinter as tk
from tkinter import filedialog

from config import PAGES, PALETTE, FONTS

from core.file_manager import FileManager

from components.page_header import PageHeader
from components.button import Button

from forms.create_form import CreateForm
from forms.message_box import MessageBox


class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        self.parent = parent
        self.configure(background=PALETTE["BACKGROUND"])

        self.rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.columnconfigure(0, weight=1)

        PageHeader(self, text="MENU GŁÓWNE").grid(row=0, column=0, ipady=30)

        Button(
            self,
            text="Utwórz zestawienie (BOM)",
            type="PRIMARY",
            command=self.create_bom,
        ).grid(row=1, column=0, ipadx=20, pady=20)

        Button(
            self,
            text="Wczytaj zestawienie (BOM)",
            type="PRIMARY",
            command=self.open_file_dialog,
        ).grid(row=2, column=0, ipadx=20, pady=20)

        Button(
            self,
            "Informacje",
            "PRIMARY",
            command=parent.switch_scene,
            arg=PAGES["CREDITS"],
        ).grid(row=3, column=0, ipadx=20, pady=20)

        Button(
            self,
            "Wyjście",
            "DANGER",
            command=parent.window.destroy,
        ).grid(row=4, column=0, ipadx=20, pady=20)

    def create_bom(self):
        create_form = CreateForm(self, self.parent)

    def open_file_dialog(self):
        file = filedialog.askopenfilename(
            title="Wybierz plik zawierajacy zestawienie",
            filetypes=(("Bompy file", "*.json"),),
        )

        try:
            file_manager = FileManager(file)

            data = file_manager.load_from_file()

            if data is None:
                MessageBox(
                    self,
                    "Błąd pliku",
                    (500, 100),
                    "Plik niezgodny z aplikacją",
                )
            else:
                self.parent.switch_scene(PAGES["WORKPAGE"])
        except:
            pass
