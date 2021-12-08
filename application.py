import tkinter as tk

from scenemanager import SceneManager
from config import BASE_CONFIG, PAGES, PALETTE


class Application(tk.Tk):
    sceneManager: None

    def __init__(self):
        tk.Tk.__init__(self)

        # main window settings
        self.title(
            f"{BASE_CONFIG['APP_NAME']} | {BASE_CONFIG['AUTHOR']} | VER: {BASE_CONFIG['VERSION']}"
        )
        self.geometry(
            f"{BASE_CONFIG['WINDOW']['DEFAULT_WIDTH']}x{BASE_CONFIG['WINDOW']['DEFAULT_HEIGHT']}"
        )

        self.minsize(
            BASE_CONFIG["WINDOW"]["MIN_WIDTH"],
            BASE_CONFIG["WINDOW"]["MIN_HEIGHT"],
        )
        self.configure(background=PALETTE["BACKGROUND"])

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        # create scene manager
        self.sceneManager = SceneManager(self)

    def run(self):
        self.mainloop()
