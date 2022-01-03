from tkinter import NSEW

from config import PAGES

from pages.menu import Menu
from pages.workpage import WorkPage
from pages.credits import Credits


# klasa zarządzająca aktualnie wyświetlaną sceną
class SceneManager:
    scene = None

    def __init__(self, window):
        self.window = window

    # metoda zmienia aktualnie wyświetlaną scenę
    def switch_scene(self, scene_index):
        scene = self.map_index_to_scene(scene_index)

        if self.scene is not None:
            self.scene.destroy()

        self.scene = scene
        self.scene.grid(row=0, column=0, sticky=NSEW)

    # metoda mapuje indeks strony na odpowiednią klasę
    def map_index_to_scene(self, index):
        if index == PAGES["MENU"]:
            return Menu(self.window)
        elif index == PAGES["WORKPAGE"]:
            return WorkPage(self.window)
        elif index == PAGES["CREDITS"]:
            return Credits(self.window)

        return None
