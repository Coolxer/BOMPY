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
from filemanager import FileManager


class WorkPage(tk.Frame):
    tree = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        fileManager = FileManager(
            "F:/CURRENT/USLUGI_SIECIOWE_W_BIZNESIE/PRO/code/target_structure.json"
        )

        data = fileManager.load_from_file()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.tree = Tree(self, data)
        self.tree.grid(column=0, row=0, sticky=tk.NSEW)
