import tkinter as tk
from tkinter import filedialog

from config import PAGES, PALETTE, FONTS

from core.filemanager import FileManager

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
            command=self.open_file_dialog,
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

    def open_file_dialog(self):
        file = filedialog.askopenfilename(
            title="Wybierz plik zawierajacy zestawienie",
            filetypes=(("Bompy file", "*.json"),),
        )

        if file is None:
            return

        file_manager = FileManager(file)
