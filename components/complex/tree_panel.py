import tkinter as tk

from config import PAGES, PALETTE, FONTS
import core.store as store

from components.button import Button

from forms.remove_dialog import RemoveDialog
from forms.edit_form import EditForm
from forms.add_form import AddForm

# klasa przycisku panelu widoku drzewa
class TreePanelButton(Button):
    def __init__(self, window, text, type, command, arg=None):
        super().__init__(window, text, type, command, arg)

        self["width"] = 5
        self["height"] = 2


# klasa panelu sterującego widokiem drzewa
class TreePanel(tk.PanedWindow):
    buttons = []

    def __init__(
        self,
        window,
    ):

        super().__init__(window)
        self.configure(background=PALETTE["BACKGROUND"])
        self.window = window
        self.buttons = []

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

    # metoda modyfikuje rozmiar i funkcjonalność panelu sterującego
    def modify_panel(self, expand):
        if expand == False:
            self.buttons[1].grid_forget()
            self.buttons[2].grid_forget()
        else:
            self.buttons[1].grid()
            self.buttons[2].grid()

    # metoda tworzy i wyświetla formularz dodawania nowego elementu
    def add_item(self):
        form = AddForm(self.window)

    # metoda tworzy i wyświetla formularz usuwania wskazanego elementu
    def remove_item(self):
        dialog = RemoveDialog(self.window)

    # metoda tworzy i wyświetla formularz edytowania wskazanego elementu
    def edit_item(self):
        form = EditForm(self.window)

    # metoda zmienia scenę na menu główne
    def back_to_menu(self):
        store.instance.get_scene_manager().switch_scene(PAGES["MENU"])
