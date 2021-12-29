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
        item,
        title,
        size,
        message,
        confirm_text,
        hide_buttons=False,
    ):
        self.data = data
        self.item = item

        tk.Frame.__init__(self, window)
        self.create_window(window, title, size, message, confirm_text)

        if not hide_buttons:
            self.show_buttons((1, 0), (1, 1))

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

    def create_window(self, window, title, size, message, confirm_text):
        self.frame = tk.Toplevel(window)
        self.frame.transient(window)
        self.frame.grab_set()

        self.frame.title(title)
        self.frame.geometry(f"{size[0]}x{size[1]}")
        self.frame.minsize(size[0], size[1])
        self.frame.maxsize(size[0], size[1])
        self.frame.config(bg=PALETTE["BACKGROUND"])

        self.frame.columnconfigure([0, 1], weight=1)
        self.frame.rowconfigure([0, 1], weight=1)

        header = SectionHeader(self.frame, message)
        header["font"] = FONTS["NORMAL_TEXT"]
        self.frame.update_idletasks()
        header.place(
            x=self.frame.winfo_width() / 2,
            y=self.frame.winfo_y() + 15,
            anchor="center",
        )

        self.confirm_btn = Button(
            self.frame, confirm_text, "PRIMARY", command=self.confirm_action
        )

        self.cancel_btn = Button(
            self.frame, "Anuluj", "DANGER", command=self.cancel_action
        )

        self.confirm_btn["width"] = self.cancel_btn["width"] = 5
        self.confirm_btn["height"] = self.cancel_btn["height"] = 2
        self.confirm_btn["font"] = self.cancel_btn["font"] = FONTS[
            "NORMAL_TEXT"
        ]

        self.define_window_geometry(size[0], size[1])

    def get_frame(self):
        return self.frame

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
