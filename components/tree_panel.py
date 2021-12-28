import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS

from components.button import Button

from forms.remove_dialog import RemoveDialog
from forms.edit_form import EditForm


class TreePanelButton(Button):
    def __init__(self, window, text, type, command, arg=None):
        super().__init__(window, text, type, command, arg)

        self["width"] = 5
        self["height"] = 2


class TreePanel(tk.PanedWindow):
    item = None
    buttons = []
    window = None

    data = {}
    item = None

    def __init__(self, window):

        super().__init__(window)
        self.window = window

        self.buttons.append(
            TreePanelButton(
                self,
                text="Usuń",
                type="PRIMARY",
                command=self.remove_item,
            )
        )

        self.buttons.append(
            TreePanelButton(
                self,
                text="Edytuj",
                type="PRIMARY",
                command=self.edit_item,
            )
        )

        self.buttons.append(
            TreePanelButton(
                self,
                text="Dodaj",
                type="PRIMARY",
                command=self.add_item,
            )
        )

        self.buttons.append(
            TreePanelButton(
                self,
                text="Menu",
                type="PRIMARY",
                command=self.back_to_menu,
            )
        )

        col = 0

        for btn in self.buttons:
            btn.set_state(tk.DISABLED)
            btn.grid(row=0, column=col, padx=5, pady=5)
            col += 1

        self.configure(background=PALETTE["BACKGROUND"])

    def set_item(self, data, item):
        self.data = data
        self.item = item

    def remove_item(self):
        # self.window.attributes("-alpha", 0.3)
        # self.window.wm_attributes("-alpha", 0.3)

        # top = tk.Toplevel(master=self.window)
        # top.wm_attributes("-alpha", 0.8)

        dialog = RemoveDialog(self.window, self.data, self.item)
        print(f"remove {self.item}")

    def edit_item(self):
        form = EditForm(self.window, self.data, self.item)
        print(f"edit {self.item}")

    def add_item(self):
        print(f"add to: {self.item}")

    def back_to_menu(self):
        print("back to menu")
