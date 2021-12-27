import tkinter as tk
from tkinter import ttk

from config import PAGES, PALETTE

from components.page_header import PageHeader
from components.section_header import SectionHeader
from components.normal_text import NormalText
from components.button import Button


class Form(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        self.tree = Tree(self, {})
        self.tree.grid(row=0, column=0)
