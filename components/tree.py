import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS

from components.tree_panel import TreePanel


class Tree(ttk.Treeview):
    panel = None
    data = {}
    idx = ""
    first = True

    def __init__(self, window, scene_manager, data):
        self.data = data
        self.idx = ""

        self.configure_style()
        super().__init__(window, style="mystyle.Treeview")
        self["selectmode"] = "browse"  # can select only one item at a time

        self.panel = TreePanel(window, scene_manager)
        self.panel.grid(row=2, column=0, sticky=tk.S)

        self.prepare_columns()
        self.service_scrollbar(window)

        # to double click on item
        # self.bind("<<TreeviewOpen>>", self.handleOpenEvent)
        self.bind("<<TreeviewSelect>>", self.handleSelectEvent)

        self.recursive(self.data)

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
            self.column(column, anchor="center")

        self.heading("identifier", text="Identyfikator")
        self.heading("quantity", text="Ilość")
        self.heading("unit", text="Jednostka")
        self.heading("unit_cost", text="Cena jedn.")
        self.heading("total_cost", text="Suma")

    def recursive(self, item):
        if len(item["sub_parts"]):
            if self.first == False:
                self.write(item)
                self.idx = item["name"]

            for el in item["sub_parts"]:
                self.recursive(el)

            if self.first == True:
                self.first = False
        else:
            self.write(item)

    def write(self, item):
        self.insert(
            self.idx,
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
        )

    def service_scrollbar(self, window):
        window.update_idletasks()  # potrzebne zeby sie dobrze pokazywala szerokosc

        vsb = ttk.Scrollbar(window, orient="vertical", command=self.yview)
        vsb.place(
            x=(window.winfo_width() - 15), y=30, height=window.winfo_height()
        )

        self.configure(yscrollcommand=vsb.set)

    # double click on item
    def handleOpenEvent(self, event):
        selected = self.focus()
        print(selected)

    def handleSelectEvent(self, event):
        selected = self.focus()

        self.panel.set_item(self.data, selected)

        for btn in self.panel.buttons:
            btn.set_state(tk.NORMAL)
