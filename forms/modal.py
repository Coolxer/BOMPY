import tkinter as tk
from tkinter import ttk

from config import PALETTE, FONTS
from components.button import Button
from components.section_header import SectionHeader


class Modal(tk.Frame):
    def __init__(self, parent):
        pass

    def define_window_geometry(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x, y
        x_pos = (screen_width / 2) - (window_width / 2)
        y_pos = (screen_height / 2) - (window_height / 2) - 10

        self.geometry(
            "%dx%d+%d+%d" % (window_width, window_height, x_pos, y_pos)
        )
