import tkinter as tk
from tkinter import ttk

from config import PALETTE

root = tk.Tk()
root.geometry("800x500")

style = ttk.Style()
style.theme_use("clam")

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
        ("selected", ("Calibri", 20, "bold")),
    ],
)

tree = ttk.Treeview(root, style="mystyle.Treeview")
tree["selectmode"] = "browse"  # can select only one item at a time

tree["columns"] = (
    "no.",
    "name",
    "identifier",
)

for column in tree["columns"]:
    tree.column(column, anchor="center")  # This will center text in rows

tree.heading("no.", text="Lp.")
tree.heading("name", text="Nazwa")
tree.heading("identifier", text="Identyfikator")

root.update_idletasks()  # potrzebne zeby sie dobrze pokazywala szerokosc

vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.place(x=(root.winfo_width() - 15), y=30, height=root.winfo_height())

tree.configure(yscrollcommand=vsb.set)

# tree.insert(parent, where_with_childs)
# na poczatku parent to wezel glowny "" zawsze tworzony i niewyswietlany
# drugi parametr okresla gdzie to wstawic wzgledem innych dzieci ---> end oznacza ze na koncu
# kolejny parametr określa taki indetyfikator aktualnie wstawionego wiersza, tak aby mozna bylo sie pozniej do niego odwolac
# pozniej juz wiadomo jest wyswietlany text
# pozniej moze byc jeszcze values=(tuple)
# inne bajery to obrazki itp
tree.insert("", "end", "A", text="A", values=(1, "pie", "#213"))
tree.insert("", "end", "B", text="B", values=(2, "dru", "#344"))
tree.insert("", "end", "C", text="C", values=(2, "dru", "#344"))
tree.insert("", "end", "D", text="D", values=(2, "dru", "#344"))
tree.insert("", "end", "E", text="E", values=(2, "dru", "#344"))
tree.insert("", "end", "F", text="F", values=(2, "dru", "#344"))
tree.insert("", "end", "G", text="G", values=(2, "dru", "#344"))
tree.insert("", "end", "H", text="H", values=(2, "dru", "#344"))
tree.insert("", "end", "I", text="I", values=(2, "dru", "#344"))
tree.insert("", "end", "J", text="J", values=(2, "dru", "#344"))
tree.insert("", "end", "K", text="K", values=(2, "dru", "#344"))
tree.insert("A", "end", "A.1", text="A.1", values=(3, "trz", "#456"))
tree.insert("A.1", "end", "A.1.1", text="A.1.1", values=(4, "czw", "#123"))
tree.insert("A", "end", "A.2", text="A.2", values=(5, "pia", "#678"))
tree.insert("A.2", "end", "A.2.1", text="A.2.1", values=(6, "szo", "#345"))

tree.insert("A.2", "end", "A.2.2", text="A.2.2", values=(7, "sio", "#568"))
tree.insert(
    "A.2.2", "end", "A.2.2.1", text="A.2.2.1", values=(7, "sio", "#568")
)
tree.insert(
    "A.2.2.1", "end", "A.2.2.1.1", text="A.2.2.1.1", values=(7, "sio", "#568")
)
tree.insert(
    "A.2.2.1.1",
    "end",
    "A.2.2.1.1.1",
    text="A.2.2.1.1.1",
    values=(7, "sio", "#568"),
)
tree.insert(
    "A.2.2.1.1.1",
    "end",
    "A.2.2.1.1.1.1",
    text="A.2.2.1.1.1.1",
    values=(7, "sio", "#568"),
)


tree.insert("B", "end", "B.1", text="B.1", values=(8, "osm", "#235"))
tree.insert("B", "end", "B.2", text="B.2", values=(9, "dzi", "#678"))
tree.insert("B.1", "end", "B.1.1", text="B.1.1", values=(10, "dzi", "#784"))


tree.pack()


def handleOpenEvent(event):
    selected = tree.focus()  # get selected item
    print(selected)

    # ewentualnie mozna uzyc tree.selection() i wtedy zwraca ci chyba razem z wartosciami (tuple)


tree.bind("<<TreeviewOpen>>", handleOpenEvent)


root.mainloop()
