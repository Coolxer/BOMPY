import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from config import PAGES, PALETTE

from components.page_header import PageHeader
from components.section_header import SectionHeader
from components.normal_text import NormalText
from components.button import Button

from components.tree import Tree

# to remove
from core.file_manager import FileManager


class WorkPage(tk.Frame):
    tree = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        self.configure(background=PALETTE["BACKGROUND"])

        file_manager = FileManager(
            "F:/CURRENT/USLUGI_SIECIOWE_W_BIZNESIE/PRO/code/target_structure.json"
        )

        data = file_manager.load_from_file()

        PageHeader(self, text=f"Zestawienie BOM dla: {data['name']}").grid(
            row=0, column=0, ipady=30
        )

        self.columnconfigure(0, weight=1)
        self.rowconfigure([0, 1], weight=1)

        # self.tree = Tree(self, data["sub_parts"])
        self.tree = Tree(self, parent, data)
        self.tree.grid(row=1, column=0, sticky=tk.NSEW)
