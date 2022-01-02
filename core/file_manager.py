import tkinter as tk
import tkinter.filedialog
import json

from config import PAGES

import core.store as store
from forms.message_box import MessageBox


class FileManager:
    def validate(self, data):
        if "application" not in data or "name" not in data:
            return False

        elif data["application"] != "bompy":
            return False

        return True

    def load(self, path=None):
        ph = store.instance.get_file_path()

        if path is not None:
            ph = path

        file = open(ph, "r")
        data = json.load(file)
        file.close()

        if not self.validate(data):
            return None

        return data

    def save(self, path=None, data=None):
        dt = store.instance.get_data()
        ph = store.instance.get_file_path()

        if path is not None:
            ph = path

        if data is not None:
            dt = data
            
        if '.json' not in ph:
            ph += '.json'

        file = open(ph, "w+")
        file.write(json.dumps(dt))
        file.close()

    def open_to_read(self, window):
        path = tk.filedialog.askopenfilename(
            title="Wybierz plik zawierajacy zestawienie",
            filetypes=(("Bompy file", "*.json"),),
        )

        if not len(path):
            return

        try:
            data = self.load(path)
        except:
            MessageBox(
                window,
                "Błąd pliku",
                (500, 100),
                "Plik niezgodny z aplikacją",
            )
            return

        store.instance.set_file_path(path)
        store.instance.set_data(data)
        store.instance.get_scene_manager().switch_scene(PAGES["WORKPAGE"])

    def open_to_write(self):
        path = tk.filedialog.asksaveasfilename(
            title="Wybierz lokalizację pliku zestawienia",
            filetypes=(("json", "*.json"),),
        )

        if not len(path):
            return

        try:
            data = {
                "application": "bumpy",
                "name": store.instance.get_project_name(),
                "sub_parts": [],
            }

            self.save(path, data)
        except:
            print("here")
            return

        store.instance.set_file_path(path)
        store.instance.set_data(data)
        store.instance.get_scene_manager().switch_scene(PAGES["WORKPAGE"])
