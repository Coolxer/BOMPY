import tkinter as tk
from tkinter import ttk

import core.store as store

from config import BASE_CONFIG, PAGES, PALETTE

# główna klasa aplikacji
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        style = ttk.Style()
        style.theme_use("clam")

        self.title(
            f"{BASE_CONFIG['APP_NAME']} | {BASE_CONFIG['AUTHOR']} | VER: {BASE_CONFIG['VERSION']}"
        )

        self.minsize(
            BASE_CONFIG["WINDOW"]["MIN_WIDTH"],
            BASE_CONFIG["WINDOW"]["MIN_HEIGHT"],
        )

        self.configure(background=PALETTE["BACKGROUND"])

        self.define_window_geometry(
            BASE_CONFIG["WINDOW"]["DEFAULT_WIDTH"],
            BASE_CONFIG["WINDOW"]["DEFAULT_HEIGHT"],
        )

        self.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.grid_columnconfigure([0], weight=1)

        store.instance.set_window(self)
        store.instance.get_scene_manager().switch_scene(PAGES["MENU"])

    # metoda definiuje rozmiar i pozycję okna aplikacji
    def define_window_geometry(self, window_width, window_height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_pos = (screen_width / 2) - (window_width / 2)
        y_pos = (screen_height / 2) - (window_height / 2) - 10

        self.geometry(
            "%dx%d+%d+%d" % (window_width, window_height, x_pos, y_pos)
        )

    # metoda uruchamia aplikację i nadsłuchiwanie zdarzeń
    def run(self):
        self.mainloop()
