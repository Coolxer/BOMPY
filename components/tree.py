import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS

from components.section_header import SectionHeader


class Tree(ttk.Treeview):
    message = None

    def __init__(self, window, data, panel):
        self.window = window
        self.data = data
        self.panel = panel
        self.parent_index = ""
        self.first_iteration = True

        self.configure_style()
        super().__init__(window, style="mystyle.Treeview")

        self["selectmode"] = "browse"  # can select only one item at a time
        self.prepare_columns()
        self.service_scrollbar(window)

        self.bind("<<TreeviewSelect>>", self.handleSelectEvent)

        self.draw()

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

    def prepare_columns(self):
        self["columns"] = (
            "identifier",
            "quantity",
            "unit",
            "unit_cost",
            "total_cost",
        )

        for column in self["columns"]:
            self.column(column, anchor="center", stretch=tk.YES, width=100)

        self.heading("identifier", text="Identyfikator")
        self.heading("quantity", text="Ilość")
        self.heading("unit", text="Jednostka")
        self.heading("unit_cost", text="Cena jedn.")
        self.heading("total_cost", text="Suma")

    def add_item(self, item):
        self.insert(
            self.parent_index,
            "end",
            item["name"],
            text=item["name"],
            values=(
                item["identifier"],
                item["quantity"],
                item["unit"],
                item["unit_cost"],
                item["total_cost"],
            ),
            open=True,
        )

    def build(self, item, parent_index=""):
        if self.first_iteration == True:
            self.first_iteration = False

            for el in item["sub_parts"]:
                self.build(el)

        else:
            self.parent_index = parent_index
            self.add_item(item)

            for el in item["sub_parts"]:
                self.build(el, item["name"])

    def draw(self):
        self.first_iteration = True
        self.delete(*self.get_all_children())
        self.build(self.data)

        if len(self.get_all_children()) == 0:
            self.grid_forget()
            self.panel.modify_panel(expand=False)
            self.message = SectionHeader(
                self.window, "Brak elementów zestawienia"
            )
            self.message.grid(row=1, column=0, ipadx=20, ipady=20)
        else:
            self.grid()
            self["height"] = len(self.get_all_children()) - 1
            self.panel.modify_panel(expand=True)
            if self.message is not None:
                self.message.grid_forget()

    def service_scrollbar(self, window):
        window.update_idletasks()  # potrzebne zeby sie dobrze pokazywala szerokosc

        vsb = ttk.Scrollbar(window, orient="vertical", command=self.yview)
        vsb.place(
            x=(window.winfo_width() - 15), y=30, height=window.winfo_height()
        )

        self.configure(yscrollcommand=vsb.set)

    def handleSelectEvent(self, event):
        selected = self.focus()

        self.panel.set_item(self.data, selected)

        for btn in self.panel.buttons:
            btn.set_state(tk.NORMAL)

    def get_all_children(self, item=""):
        children = self.get_children(item)
        for child in children:
            children += self.get_all_children(child)
        return children
