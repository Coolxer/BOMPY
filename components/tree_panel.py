import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS, PAGES

from components.button import Button

from forms.remove_dialog import RemoveDialog
from forms.edit_form import EditForm
from forms.add_form import AddForm


class TreePanelButton(Button):
    def __init__(self, window, text, type, command, arg=None):
        super().__init__(window, text, type, command, arg)

        self["width"] = 5
        self["height"] = 2


class TreePanel(tk.PanedWindow):
    item = None
    buttons = []
    data = {}
    item = None

    def __init__(self, window, scene_manager):

        super().__init__(window)
        self.window = window
        self.scene_manager = scene_manager

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
                text="Edytuj",
                type="PRIMARY",
                command=self.edit_item,
            )
        )

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

        self.buttons[len(self.buttons) - 1].set_state(tk.NORMAL)

        self.configure(background=PALETTE["BACKGROUND"])

    def set_refresh_callback(self, refresh_callback):
        self.refresh_callback = refresh_callback

    def set_item(self, data, item):
        self.data = data
        self.item = item

    def modify_panel(self, expand):
        if expand == False:
            self.buttons[1].grid_forget()
            self.buttons[2].grid_forget()
        else:
            self.buttons[1].grid()
            self.buttons[2].grid()

    def add_item(self):
        form = AddForm(self.window, self.data, self.item)
        print(f"add to: {self.item}")

    def remove_item(self):
        print(f"remove {self.item}")
        dialog = RemoveDialog(
            self.window, self.data, self.item, self.refresh_callback
        )

    def edit_item(self):
        form = EditForm(self.window, self.data, self.item)
        print(f"edit {self.item}")

    def back_to_menu(self):
        print("back to menu")
        self.scene_manager.switch_scene(PAGES["MENU"])
