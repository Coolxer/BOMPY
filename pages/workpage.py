import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from config import PAGES, PALETTE
import core.store as store

from components.page_header import PageHeader
from components.section_header import SectionHeader
from components.normal_text import NormalText
from components.button import Button

from components.tree import Tree
from components.tree_panel import TreePanel


class WorkPage(tk.Frame):
    tree = None

    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.configure(background=PALETTE["BACKGROUND"])

        PageHeader(
            self,
            # text=f"Zestawienie BOM dla: {store.instance.get_data()['name']}",
            text="Zestawienie BOM dla",
        ).grid(row=0, column=0, ipady=30)

        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure(0, weight=1)

        panel = TreePanel(self)
        tree = Tree(self, panel)

        panel.set_refresh_callback(tree.draw)

        if not tree.is_empty():
            tree.grid(row=1, column=0, ipadx=20, ipady=20)

        panel.grid(row=2, column=0, sticky=tk.S, pady=30)
