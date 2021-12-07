import tkinter as tk

from config import CONFIG


class Application(tk.Frame):
    def __init__(self, *args, **kwargs):
        self.root = tk.Tk()

        tk.Frame.__init__(self, self.root, *args, **kwargs)

        self.root.title(
            f"{CONFIG['APP_NAME']} | {CONFIG['AUTHOR']} | VER: {CONFIG['VERSION']}"
        )
        self.root.geometry(
            f"{CONFIG['DEFAULT_WIDTH']}x{CONFIG['DEFAULT_HEIGHT']}"
        )

    def run(self):
        self.root.mainloop()
