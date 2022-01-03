import tkinter as tk

from config import PAGES, PALETTE
import core.store as store

from components.text import PageHeader, SectionHeader, NormalText
from components.button import Button

# Strona informacyjna aplikacji
class Credits(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, window)

        self.configure(background=PALETTE["BACKGROUND"])
        self.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.grid_columnconfigure([0], weight=1)

        PageHeader(self, text="INFORMACJE").grid(row=0, column=0, ipady=30)

        # o aplikacji
        SectionHeader(self, text="O aplikacji").grid(
            row=1, column=0, pady=(20, 0)
        )
        NormalText(
            self,
            text="Aplikacja powstała w ramach projektu z przedmiotu 'Usługi sieciowe w biznesie'. Program umożliwia przegląd i modyfikację zestawień materiałowych BOM, ułatwiających funkcjonowanie przedsiębiorstw. Aplikacja posiada wygodny i intuicyjny interfejs użytkownika, system zapisywania i wczytywania zestawień, możliwość wygodnego przeglądania zestawień poprzez wykorzystanie hierachicznego drzewa widoku, a także przyjazny system tworzenia i edycji zestawień.",
        ).grid(row=2, column=0)

        # o autorze
        SectionHeader(self, text="O autorze").grid(
            row=3, column=0, pady=(20, 0)
        )
        NormalText(self, text="Łukasz Miłoś, 4EF-ZI, 161883").grid(
            row=4, column=0
        )

        # linki
        SectionHeader(self, text="Linki").grid(row=5, column=0, pady=(20, 0))
        NormalText(
            self, text="Kod źródłowy: https://github.com/Coolxer/BOMPY"
        ).grid(row=6, column=0)
        NormalText(
            self,
            text="Dokumentacja projektowa: https://github.com/Coolxer/BOMDOC",
        ).grid(row=7, column=0)

        Button(
            self,
            text="Powrót do menu",
            type="PRIMARY",
            command=store.instance.get_scene_manager().switch_scene,
            arg=PAGES["MENU"],
        ).grid(row=8, column=0, pady=50)
