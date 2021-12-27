import tkinter as tk
from tkinter import ttk
from config import PALETTE, FONTS

from components.tree_panel import TreePanel


class Tree(ttk.Treeview):
    data = {}
    idx = ""

    def __init__(self, window, data):
        self.configure_style()

        super().__init__(window, style="mystyle.Treeview")

        self["selectmode"] = "browse"  # can select only one item at a time

        self.prepare_columns()
        self.service_scrollbar(window)

        self.bind("<<TreeviewOpen>>", self.handleOpenEvent)

        self.pass_data(data)

        TreePanel(window).grid(column=0, row=0, sticky=tk.S)

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
            "name",
            "identifier",
            "quantity",
            "unit",
            "unit_cost",
            "total_cost",
        )

        for column in self["columns"]:
            self.column(column, anchor="center")

        self.heading("name", text="Nazwa")
        self.heading("identifier", text="Identyfikator")
        self.heading("quantity", text="Ilość")
        self.heading("unit", text="Jednostka")
        self.heading("unit_cost", text="Cena jedn.")
        self.heading("total_cost", text="Suma")

    def pass_data(self, data):
        self.data = data
        self.idx = ""
        self.recursive(self.data)

    def recursive(self, element):
        if len(element["sub_parts"]):
            self.write(element)

            self.idx = element["name"]

            for el in element["sub_parts"]:
                self.recursive(el)
        else:
            self.write(element)

    def write(self, element):
        self.insert(
            self.idx,
            "end",
            element["name"],
            text=element["name"],
            values=(
                element["name"],
                element["identifier"],
                element["quantity"],
                element["unit"],
                element["unit_cost"],
                element["total_cost"],
            ),
        )

    def service_scrollbar(self, window):
        window.update_idletasks()  # potrzebne zeby sie dobrze pokazywala szerokosc

        vsb = ttk.Scrollbar(window, orient="vertical", command=self.yview)
        vsb.place(
            x=(window.winfo_width() - 15), y=30, height=window.winfo_height()
        )

        self.configure(yscrollcommand=vsb.set)

    def handleOpenEvent(self, event):
        selected = self.focus()
        print(selected)
