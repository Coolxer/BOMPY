import tkinter as tk
import tkinter.filedialog
import json

from config import PAGES

import core.store as store
from forms.message_box import MessageBox

# klasa obsługi plików
class FileManager:

    # metoda sprawdza poprawność pliku wejściowego (zgodny z aplikacją)
    def validate(self, data):
        if "application" not in data or "name" not in data:
            return False

        elif data["application"] != "bompy" or not len(data["name"]):
            return False

        return True

    # metoda wczytuje dane z pliku
    def load(self, path=None):
        ph = store.instance.get_file_path()

        if path is not None:
            ph = path

        with open(ph, encoding="utf-8") as file:
            data = json.load(file)

        if not self.validate(data):
            return None

        return data

    # metoda zapisuje dane do pliku
    def save(self, path=None, data=None):
        dt = store.instance.get_data()
        ph = store.instance.get_file_path()

        if path is not None:
            ph = path

        if data is not None:
            dt = data

        if ".json" not in ph:
            ph += ".json"

        file = open(ph, "w+")
        file.write(json.dumps(dt))
        file.close()

    # metoda otwiera okno do wyboru pliku do odczytu
    def open_to_read(self, window):
        path = tk.filedialog.askopenfilename(
            title="Wybierz plik zawierajacy zestawienie",
            filetypes=(("Bompy file", "*.json"),),
        )

        if not len(path):
            return

        data = {}

        try:
            data = self.load(path)
            if not data:
                raise Exception()
        except:
            MessageBox(
                window,
                "Błąd pliku",
                (500, 100),
                "Plik niezgodny z aplikacją",
            )
            return

        store.instance.set_file_path(path)
        store.instance.set_project_name(data["name"])
        store.instance.set_data(data)
        store.instance.get_scene_manager().switch_scene(PAGES["WORKPAGE"])

    # metoda otwiera okno do wyboru pliku do zapisu
    def open_to_write(self):
        path = tk.filedialog.asksaveasfilename(
            title="Wybierz lokalizację pliku zestawienia",
            filetypes=(("Bompy file", "*.json"),),
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
            return

        store.instance.set_file_path(path)
        store.instance.set_data(data)
        store.instance.get_scene_manager().switch_scene(PAGES["WORKPAGE"])
