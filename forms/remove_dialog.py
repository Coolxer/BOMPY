import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.button import Button
from components.section_header import SectionHeader


class RemoveDialog(tk.Frame):
    frame = None
    data = {}
    item = None

    def __init__(self, parent, data, item):
        self.data = data
        self.item = item

        tk.Frame.__init__(self, parent)
        self.create_window(parent)

    def confirm(self):
        for item in self.data:
            if "name" in element and self.data[self.item]:
                item.pop("name", None)

        print(data)
        self.frame.destroy()

    def cancel(self):
        print("cancel")
        self.frame.destroy()

    def define_window_geometry(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_pos = (screen_width / 2) - (window_width / 2)
        y_pos = (screen_height / 2) - (window_height / 2) - 10

        self.frame.geometry(
            "%dx%d+%d+%d" % (window_width, window_height, x_pos, y_pos)
        )

    def create_window(self, window):
        self.frame = tk.Toplevel(window)
        self.frame.transient(window)
        self.frame.grab_set()

        self.frame.title("Usuwanie obiektu")
        self.frame.geometry("400x100")
        self.frame.minsize(400, 100)
        self.frame.maxsize(400, 100)
        self.frame.config(bg=PALETTE["BACKGROUND"])

        self.frame.columnconfigure([0, 1], weight=1)
        self.frame.rowconfigure([0, 1], weight=1)

        header = SectionHeader(
            self.frame, "Czy jesteś pewien, że chcesz usunąć ten obiekt?"
        )
        header["font"] = FONTS["NORMAL_TEXT"]
        self.frame.update_idletasks()
        header.place(
            x=self.frame.winfo_width() / 2,
            y=self.frame.winfo_y() + 15,
            anchor="center",
        )

        confirm_btn = Button(self.frame, "Usuń", "DANGER", command=self.confirm)
        confirm_btn.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

        cancel_btn = Button(
            self.frame, "Anuluj", "PRIMARY", command=self.cancel
        )
        cancel_btn.grid(row=1, column=1, sticky=tk.E, padx=10, pady=10)

        confirm_btn["width"] = cancel_btn["width"] = 5
        confirm_btn["height"] = cancel_btn["height"] = 2
        confirm_btn["font"] = cancel_btn["font"] = FONTS["NORMAL_TEXT"]

        self.define_window_geometry(400, 100)
