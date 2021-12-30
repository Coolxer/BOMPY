import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.button import Button
from components.section_header import SectionHeader


class Modal(tk.Frame):
    def __init__(
        self,
        window,
        data,
        item_name,
        title,
        size,
        message,
        confirm_text,
        hide_buttons=False,
        rows=[0, 1],
        columns=[0, 1, 2],
    ):
        self.data = data
        self.item_name = item_name

        tk.Frame.__init__(self, window)
        self.create_window(
            window, title, size, message, confirm_text, rows, columns
        )

        if not hide_buttons:
            self.show_buttons((1, 0), (1, 2))
            
    def get_data(self):
        return self.data
    
    def get_item_name(self):
        return self.item_name

    def confirm_action(self):
        self.confirm()
        self.frame.destroy()

    def cancel_action(self):
        self.cancel()
        self.frame.destroy()

    def confirm(self):
        pass

    def cancel(self):
        pass

    def define_window_geometry(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_pos = (screen_width / 2) - (window_width / 2)
        y_pos = (screen_height / 2) - (window_height / 2) - 10

        self.frame.geometry(
            "%dx%d+%d+%d" % (window_width, window_height, x_pos, y_pos)
        )

    def create_window(
        self, window, title, size, message, confirm_text, rows, columns
    ):
        self.frame = tk.Toplevel(window)
        self.frame.transient(window)
        self.frame.grab_set()

        self.frame.title(title)
        self.frame.geometry(f"{size[0]}x{size[1]}")
        self.frame.minsize(size[0], size[1])
        self.frame.maxsize(size[0], size[1])
        self.frame.config(bg=PALETTE["BACKGROUND"])

        self.frame.rowconfigure(rows, weight=1)
        self.frame.columnconfigure(columns, weight=1)

        header = SectionHeader(self.frame, message)
        header["font"] = FONTS["COMPONENT"]
        header.grid(row=0, column=1, ipadx=5, ipady=5)

        self.confirm_btn = Button(
            self.frame, confirm_text, "PRIMARY", command=self.confirm_action
        )

        self.cancel_btn = Button(
            self.frame, "Anuluj", "DANGER", command=self.cancel_action
        )

        self.confirm_btn["width"] = self.cancel_btn["width"] = 8
        self.confirm_btn["height"] = self.cancel_btn["height"] = 2
        self.confirm_btn["font"] = self.cancel_btn["font"] = FONTS["COMPONENT"]

        self.define_window_geometry(size[0], size[1])

    def show_buttons(self, cf_btn_pos, cn_btn_pos):
        self.confirm_btn.grid(
            row=cf_btn_pos[0],
            column=cf_btn_pos[1],
            sticky=tk.W,
            padx=10,
            pady=10,
        )
        self.cancel_btn.grid(
            row=cn_btn_pos[0],
            column=cn_btn_pos[1],
            sticky=tk.E,
            padx=10,
            pady=10,
        )

    def get_frame(self):
        return self.frame
