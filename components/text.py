from tkinter import Label

from config import PALETTE, FONTS


class Text(Label):
    def __init__(self, window, font, text, color=PALETTE["PRIMARY"]):
        super().__init__(window)

        self["text"] = text
        self["foreground"] = color
        self["background"] = PALETTE["BACKGROUND"]
        self["font"] = font
        self["wraplength"] = 500


class PageHeader(Text):
    def __init__(self, window, text):
        super().__init__(window, font=FONTS["PAGE_HEADER"], text=text)


class SectionHeader(Text):
    def __init__(self, window, text):
        super().__init__(window, font=FONTS["SECTION_HEADER"], text=text)


class NormalText(Text):
    def __init__(self, window, text):
        super().__init__(
            window, font=FONTS["NORMAL_TEXT"], text=text, color=PALETTE["WHITE"]
        )
