from tkinter import Label

from config import PALETTE, FONTS

# klasa bazowa tekstu
class Text(Label):
    def __init__(self, window, font, text, color=PALETTE["PRIMARY"]):
        super().__init__(window)

        self["text"] = text
        self["foreground"] = color
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = font
        self["wraplength"] = 500


# klasa nagłówka strony aplikacji
class PageHeader(Text):
    def __init__(self, window, text):
        super().__init__(window, font=FONTS["PAGE_HEADER"], text=text)


# klasa nagłówka sekcji strony
class SectionHeader(Text):
    def __init__(self, window, text):
        super().__init__(window, font=FONTS["SECTION_HEADER"], text=text)


# klasa zwykłego tekstu
class NormalText(Text):
    def __init__(self, window, text):
        super().__init__(
            window, font=FONTS["NORMAL_TEXT"], text=text, color=PALETTE["WHITE"]
        )
