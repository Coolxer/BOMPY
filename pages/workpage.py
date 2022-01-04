import tkinter as tk

from config import PAGES, PALETTE
import core.store as store

from components.text import PageHeader, SectionHeader, NormalText
from components.button import Button

from components.complex.tree import Tree
from components.complex.tree_panel import TreePanel

# strona główna zestawienia BOM
class WorkPage(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.configure(background=PALETTE["BACKGROUND"])
        self.rowconfigure([0, 1], weight=1)
        self.columnconfigure([0], weight=1)

        panel = TreePanel(self)
        tree = Tree(self, panel)

        store.instance.set_refresh_callback(tree.draw)
        store.instance.set_child_func(tree.get_all_children)

        PageHeader(
            self,
            text=store.instance.get_project_name().upper(),
        ).grid(row=0, column=0, ipady=30)

        tree.grid(row=1, column=0, ipady=20)
        panel.grid(row=2, column=0, sticky=tk.S, pady=30)
