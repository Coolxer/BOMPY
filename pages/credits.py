import tkinter as tk

from config import PAGES, PALETTE

from components.page_header import PageHeader
from components.section_header import SectionHeader
from components.normal_text import NormalText
from components.button import Button


class Credits(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent.window)

        self.configure(background=PALETTE["BACKGROUND"])

        PageHeader(self, text="Informacje").grid(column=0, row=0, ipady=50)

        SectionHeader(self, text="O aplikacji").grid(
            column=0, row=1, pady=(20, 0)
        )
        NormalText(
            self,
            text="Aplikacja powstała w ramach projektu z przedmiotu 'Usługi sieciowe w biznesie'. Program umożliwia przegląd i modyfikację zestawień materiałowych BOM, ułatwiających funkcjonowanie przedsiębiorstw. Aplikacja posiada wygodny i intuicyjny interfejs użytkownika, system zapisywania i wczytywania zestawień, możliwość wygodnego przeglądania zestawień poprzez wykorzystanie hierachicznego drzewa widoku, a także przyjazny system tworzenia i edycji zestawień.",
        ).grid(column=0, row=2)

        SectionHeader(self, text="O autorze").grid(
            column=0, row=3, pady=(20, 0)
        )
        NormalText(self, text="Łukasz Miłoś, 4EF-ZI, 161883").grid(
            column=0, row=4
        )

        SectionHeader(self, text="Linki").grid(column=0, row=5, pady=(20, 0))
        NormalText(
            self, text="Kod źródłowy: https://github.com/Coolxer/BOMPY"
        ).grid(column=0, row=6)
        NormalText(
            self,
            text="Dokumentacja projektowa: https://github.com/Coolxer/BOMDOC",
        ).grid(column=0, row=7)

        Button(
            self,
            text="Powrót do menu",
            type="PRIMARY",
            action=parent.switch_scene,
            arg=PAGES["MENU"],
        ).grid(column=0, row=8, pady=50)
