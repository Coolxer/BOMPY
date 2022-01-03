from forms.object_form import ObjectForm

import core.store as store

# klasa formularza dodawania nowego elementu
class AddForm(ObjectForm):
    def __init__(self, window):
        super().__init__(
            window=window,
            title="Dodawanie obiektu",
            size=(600, 400),
            message="Dodawanie obiektu",
            confirm_text="Dodaj",
        )

        super().set_submit_action(self.submit)

    # metoda dodaje element do listy
    def submit(self, el, item, result):
        it = super().get_form_values()
        it["sub_parts"] = []
        el["sub_parts"].append(it)
