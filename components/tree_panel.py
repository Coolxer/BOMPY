import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS

from components.button import Button


class TreePanelButton(Button):
    def __init__(self, window, text, type, action, arg=None):
        super().__init__(window, text, type, action, arg)

        self["width"] = 5
        self["height"] = 2


class TreePanel(tk.PanedWindow):
    def __init__(self, window):

        super().__init__(window)

        TreePanelButton(
            self,
            text="Usuń",
            type="PRIMARY",
            action=self.remove_element,
        ).grid(column=0, row=0, padx=5, pady=5)

        TreePanelButton(
            self,
            text="Edytuj",
            type="PRIMARY",
            action=self.remove_element,
        ).grid(column=1, row=0, padx=5, pady=5)

        TreePanelButton(
            self,
            text="Dodaj",
            type="PRIMARY",
            action=self.add_element,
        ).grid(column=2, row=0, padx=5, pady=5)

        TreePanelButton(
            self,
            text="Menu",
            type="PRIMARY",
            action=self.back_to_menu,
        ).grid(column=4, row=0, padx=5, pady=5)

    def remove_element(self, element):
        print("remove")

    def edit_element(self, element):
        print("edit")

    def add_element(self, element):
        print("add")

    def back_to_menu(self):
        print("back to menu")
