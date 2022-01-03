import tkinter as tk
from tkinter import ttk

from config import PAGES, PALETTE, FONTS
import core.store as store

from components.text import SectionHeader
from forms.message_box import MessageBox

MAX_DISPLAYING_ITEMS = 10

# klasa widoku drzewa
class Tree(ttk.Treeview):
    scrollbar = None

    def __init__(self, window, panel):
        self.window = window
        self.panel = panel
        self.parent_id = ""
        self.first_iteration = True

        self.configure_style()
        super().__init__(window, style="mystyle.Treeview")

        self["selectmode"] = "browse"
        self.prepare_columns()
        self.service_scrollbar(window)

        self.bind("<<TreeviewSelect>>", self.handleSelectEvent)
        self.draw()

    # metoda ustawia styl dla widoku drzewa
    def configure_style(self):
        style = ttk.Style()

        style.configure(
            "mystyle.Treeview",
            highlightthickness=0,
            bd=0,
            font=("Calibri", 13),
            background=PALETTE["BACKGROUND"],
            foreground=PALETTE["WHITE"],
            rowheight=40,
        )

        style.configure(
            "mystyle.Treeview.Heading",
            font=("Calibri", 13, "bold"),
            background=PALETTE["PRIMARY"],
            foreground=PALETTE["BACKGROUND"],
            anchor=tk.CENTER,
        )

        style.map(
            "Treeview",
            background=[
                ("background", PALETTE["BACKGROUND"]),
                ("selected", PALETTE["PRIMARY"]),
            ],
            foreground=[
                ("background", PALETTE["WHITE"]),
                ("selected", PALETTE["BACKGROUND"]),
            ],
            font=[
                ("background", ("Calibri", 13, "bold")),
                ("selected", ("Calibri", 18, "bold")),
            ],
        )

    # metoda przygotowuje kolumny dla widoku
    def prepare_columns(self):
        self["columns"] = (
            "name",
            "quantity",
            "unit",
            "unit_cost",
            "total_cost",
        )

        for column in self["columns"]:
            self.column(column, anchor="center", stretch=tk.YES, width=100)

        self.heading("name", text="Nazwa")
        self.heading("quantity", text="Ilość")
        self.heading("unit", text="Jednostka")
        self.heading("unit_cost", text="Cena jedn.")
        self.heading("total_cost", text="Suma")

    # metoda dodaje element do drzewa o odpowiednim stopniu zagnieżdżenia
    def add_item(self, item):
        try:
            self.insert(
                self.parent_id,
                "end",
                item["identifier"],
                text=item["identifier"],
                values=(
                    item["name"],
                    item["quantity"],
                    item["unit"],
                    item["unit_cost"],
                    int(item["quantity"] * float(item["unit_cost"])),
                ),
                open=True,
            )
        except:
            MessageBox(
                self.window,
                "Błąd pliku",
                (500, 100),
                "Błąd zestawienia (zduplikowany identyfikator) / brak wartości",
                store.instance.get_scene_manager().switch_scene,
                PAGES["MENU"],
            )

    # metoda rekurencyjna przeszukiwania obiektu i dodająca element do drzewa
    def build(self, item, parent_id=""):
        if self.first_iteration == True:
            self.first_iteration = False

            for el in item["sub_parts"]:
                self.build(el)

        else:
            self.parent_id = parent_id
            self.add_item(item)

            for el in item["sub_parts"]:
                self.build(el, item["identifier"])

    # metoda przerysowuje drzewo widoku
    def draw(self):
        self.first_iteration = True
        self.delete(*self.get_all_children())
        self.build(store.instance.get_data())

        self.insert(
            "",
            0,
            "#",
            text="",
            values=("", "", "", "", ""),
        )

        items = len(self.get_all_children()) - 1

        if items < MAX_DISPLAYING_ITEMS:
            self["height"] = items
        else:
            self["height"] = MAX_DISPLAYING_ITEMS

        self.panel.modify_panel(expand=True)

    # metoda obsługuje pasek przewijania dla widoku drzewa
    def service_scrollbar(self, window):
        window.update_idletasks()

        self.scrollbar = ttk.Scrollbar(
            window, orient="vertical", command=self.yview
        )
        self.scrollbar.grid(row=1, column=2, sticky=tk.NSEW, padx=30)

        self.configure(yscrollcommand=self.scrollbar.set)

    # metoda obsługuje zdarzenie wyboru elementu drzewa
    def handleSelectEvent(self, event):
        selected = self.focus()
        store.instance.set_item(self.item(selected), selected)

        if selected == "#":
            self.panel.buttons[0].set_state(tk.NORMAL)
            self.panel.buttons[1].set_state(tk.DISABLED)
            self.panel.buttons[2].set_state(tk.DISABLED)
            self.panel.buttons[3].set_state(tk.NORMAL)

        else:
            for btn in self.panel.buttons:
                btn.set_state(tk.NORMAL)

    # metoda zwraca wszystkie elementy drzewa, w tym zagnieżdżone
    def get_all_children(self, item=""):
        children = self.get_children(item)
        for child in children:
            children += self.get_all_children(child)
        return children
