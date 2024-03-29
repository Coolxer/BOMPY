import tkinter as tk
import tkinter.filedialog

from config import PAGES, PALETTE, FONTS
import core.store as store
from core.file_manager import FileManager

from components.text import PageHeader
from components.button import Button

from forms.create_form import CreateForm
from forms.message_box import MessageBox

# menu główne aplikacji
class Menu(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.configure(background=PALETTE["BACKGROUND"])
        self.rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.columnconfigure(0, weight=1)

        scene_manager = store.instance.get_scene_manager()
        file_manager = store.instance.get_file_manager()

        PageHeader(self, text="MENU GŁÓWNE").grid(row=0, column=0, ipady=30)

        Button(
            self,
            text="Utwórz zestawienie (BOM)",
            type="PRIMARY",
            command=CreateForm,
            arg=window,
        ).grid(row=1, column=0, ipadx=20, pady=20)

        Button(
            self,
            text="Wczytaj zestawienie (BOM)",
            type="PRIMARY",
            command=file_manager.open_to_read,
            arg=window,
        ).grid(row=2, column=0, ipadx=20, pady=20)

        Button(
            self,
            "Informacje",
            "PRIMARY",
            command=scene_manager.switch_scene,
            arg=PAGES["CREDITS"],
        ).grid(row=3, column=0, ipadx=20, pady=20)

        Button(
            self,
            "Wyjście",
            "DANGER",
            command=window.destroy,
        ).grid(row=4, column=0, ipadx=20, pady=20)
