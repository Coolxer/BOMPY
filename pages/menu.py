import tkinter as tk
from tkinter import filedialog

from config import PAGES, PALETTE, FONTS

from filemanager import FileManager

from components.page_header import PageHeader
from components.button import Button

class Menu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        self.configure(background=PALETTE["BACKGROUND"])

        PageHeader(self, text="MENU GŁÓWNE").grid(column=0, row=0, ipady=50)

        Button(
            self,
            text="Utwórz zestawienie (BOM)",
            type="PRIMARY",
            action=self.open_file_dialog,
        ).grid(column=0, row=1, ipadx=20, pady=20)

        Button(
            self,
            text="Wczytaj zestawienie (BOM)",
            type="PRIMARY",
            action=self.open_file_dialog,
        ).grid(column=0, row=2, ipadx=20, pady=20)

        Button(
            self,
            "Informacje",
            "PRIMARY",
            action=parent.switch_scene,
            arg=PAGES["CREDITS"],
        ).grid(column=0, row=3, ipadx=20, pady=20)

        Button(
            self,
            "Wyjście",
            "DANGER",
            action=parent.window.destroy,
        ).grid(column=0, row=4, ipadx=20, pady=20)

    def open_file_dialog(self):
        file = filedialog.askopenfilename(
            title="Wybierz plik zawierajacy zestawienie",
            filetypes=(("Bompy file", "*.json"),),
        )

        if file is None:
            return

        file_manager = FileManager(file)
