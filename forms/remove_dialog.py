from forms.modal import Modal
import core.store as store

# klasa reprezentująca okno potwierdzające chęć usunięcia obiektu
class RemoveDialog(Modal):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Usuwanie obiektu",
            size=(500, 100),
            message="Czy chcesz usunąć ten obiekt?",
            confirm_text="Usuń",
            lookup=True,
        )

    # metoda usuwa element z listy
    def confirm(self, el=None, item=None, result=None):
        item["sub_parts"].pop(result)
