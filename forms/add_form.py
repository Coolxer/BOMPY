from forms.object_form import ObjectForm

import core.store as store

# klasa formularza dodawania nowego elementu
class AddForm(ObjectForm):
    def __init__(self, window, add_callback):
        super().__init__(
            window=window,
            title="Dodawanie obiektu",
            size=(600, 400),
            message="Dodawanie obiektu",
            confirm_text="Dodaj",
        )

        self.add_callback = add_callback

        super().set_accept_action(self.accept)

    # metoda dodająca element do listy
    def accept(self):
        self.recursive_lookup(store.instance.get_data())
        store.instance.get_file_manager().save()
        self.add_callback()

    # metoda przeszukująca listę w celu znalezienia odpowiedniego miejsca na wstawienie elementu
    def recursive_lookup(self, item, index=0):
        if (
            "identifier" in item
            and item["identifier"] == store.instance.get_identifier()
        ):
            return index

        index = 0
        for el in item["sub_parts"]:
            result = self.recursive_lookup(el, index)
            if result >= 0:
                it = super().get_form_values()
                it["sub_parts"] = []

                el["sub_parts"].append(it)

            index += 1

        return -1
