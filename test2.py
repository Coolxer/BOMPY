import json

from tkinter import Tk
from components.tree import Tree
from filemanager import FileManager


"""
class Element:
    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def get_property(self, property):
        return self.obj[property]


# el = Element(string)
# print(el.get_property("total_cost"))
"""

fileManager = FileManager(
    "F:/CURRENT/USLUGI_SIECIOWE_W_BIZNESIE/PRO/code/target_structure.json"
)

data = fileManager.load_from_file()

root = Tk()
tree = Tree(root, data)
tree.grid(row=0, column=0)

root.mainloop()
