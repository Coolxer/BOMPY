from tkinter import NSEW

from pages.menu import Menu
from pages.workpage import WorkPage
from pages.credits import Credits

from config import PAGES


class SceneManager:
    window = None
    scene = None

    def __init__(self, window):
        self.window = window

    def switch_scene(self, scene_index):
        scene = self.map_index_to_scene(scene_index)

        if self.scene is not None:
            self.scene.destroy()

        self.scene = scene
        self.scene.grid(row=0, column=0, sticky=NSEW)

    def map_index_to_scene(self, index):
        if index == PAGES["MENU"]:
            return Menu(self.window)
        elif index == PAGES["WORKPAGE"]:
            return WorkPage(self.window)
        elif index == PAGES["CREDITS"]:
            return Credits(self.window)

        return None
